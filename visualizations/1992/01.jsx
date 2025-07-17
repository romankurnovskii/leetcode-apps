import React, {useState, useEffect, useMemo} from "react";

// --- Helper Components ---

// Icon for the play/pause button
const PlayIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="24"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <polygon points="5 3 19 12 5 21 5 3"></polygon>
  </svg>
);

// Icon for the pause button
const PauseIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="24"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <rect x="6" y="4" width="4" height="16"></rect>
    <rect x="14" y="4" width="4" height="16"></rect>
  </svg>
);

// --- Main App Component ---

export default function App() {
  // --- State Management ---
  const [land, setLand] = useState([
    [1, 0, 0],
    [0, 1, 1],
    [0, 1, 1],
  ]);
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [foundFarmlands, setFoundFarmlands] = useState([]);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(500); // milliseconds

  // --- Algorithm & Visualization Logic ---

  // Memoize the generation of visualization steps to avoid re-running on every render.
  const generateVisualization = useMemo(() => {
    return (matrix) => {
      const steps = [];
      const found = [];
      const rows = matrix.length;
      const cols = matrix[0].length;
      const visited = Array(rows)
        .fill(false)
        .map(() => Array(cols).fill(false));

      // Initial state
      steps.push({
        grid: JSON.parse(JSON.stringify(matrix)),
        visited: JSON.parse(JSON.stringify(visited)),
        highlight: null,
        currentFarm: null,
        message: "Algorithm starting. Scanning for farmland.",
        found: [],
      });

      for (let r1 = 0; r1 < rows; r1++) {
        for (let c1 = 0; c1 < cols; c1++) {
          // Highlight the currently scanned cell
          steps.push({
            grid: JSON.parse(JSON.stringify(matrix)),
            visited: JSON.parse(JSON.stringify(visited)),
            highlight: {r: r1, c: c1, type: "scan"},
            currentFarm: null,
            message: `Scanning cell [${r1}, ${c1}].`,
            found: [...found],
          });

          if (matrix[r1][c1] === 1 && !visited[r1][c1]) {
            // Found the top-left corner of a new farmland
            steps.push({
              grid: JSON.parse(JSON.stringify(matrix)),
              visited: JSON.parse(JSON.stringify(visited)),
              highlight: {r: r1, c: c1, type: "found-start"},
              currentFarm: {r1, c1, r2: r1, c2: c1},
              message: `Found top-left corner of a new farm at [${r1}, ${c1}].`,
              found: [...found],
            });

            let r2 = r1;
            let c2 = c1;

            // Find the bottom-most row of the current farm
            while (r2 + 1 < rows && matrix[r2 + 1][c1] === 1) {
              r2++;
            }
            // Find the right-most column of the current farm
            while (c2 + 1 < cols && matrix[r1][c2 + 1] === 1) {
              c2++;
            }

            steps.push({
              grid: JSON.parse(JSON.stringify(matrix)),
              visited: JSON.parse(JSON.stringify(visited)),
              highlight: null,
              currentFarm: {r1, c1, r2, c2},
              message: `Expanding to find bottom-right corner. Found at [${r2}, ${c2}].`,
              found: [...found],
            });

            found.push([r1, c1, r2, c2]);

            // Mark all cells in this farmland as visited
            for (let i = r1; i <= r2; i++) {
              for (let j = c1; j <= c2; j++) {
                visited[i][j] = true;
              }
            }

            steps.push({
              grid: JSON.parse(JSON.stringify(matrix)),
              visited: JSON.parse(JSON.stringify(visited)),
              highlight: null,
              currentFarm: {r1, c1, r2, c2},
              message: `Marking farm [${r1},${c1}] to [${r2},${c2}] as visited. Added to results.`,
              found: [...found],
            });
          }
        }
      }

      steps.push({
        grid: JSON.parse(JSON.stringify(matrix)),
        visited: JSON.parse(JSON.stringify(visited)),
        highlight: null,
        currentFarm: null,
        message: "Algorithm finished. All farmlands found.",
        found: [...found],
      });

      return {steps, result: found};
    };
  }, []);

  // --- Effects ---

  // Re-run visualization when the input grid changes
  useEffect(() => {
    const {steps, result} = generateVisualization(land);
    setVisualizationSteps(steps);
    setFoundFarmlands(result);
    setCurrentStep(0);
    setIsPlaying(false);
  }, [land, generateVisualization]);

  // Auto-play interval
  useEffect(() => {
    if (isPlaying) {
      const interval = setInterval(() => {
        setCurrentStep((prevStep) => {
          if (prevStep < visualizationSteps.length - 1) {
            return prevStep + 1;
          }
          setIsPlaying(false);
          return prevStep;
        });
      }, speed);
      return () => clearInterval(interval);
    }
  }, [isPlaying, speed, visualizationSteps.length]);

  // --- Event Handlers ---
  const handleNext = () => {
    if (currentStep < visualizationSteps.length - 1) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handlePrevious = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleReset = () => {
    setCurrentStep(0);
    setIsPlaying(false);
  };

  const handlePlayPause = () => {
    if (currentStep === visualizationSteps.length - 1) {
      setCurrentStep(0);
      setIsPlaying(true);
    } else {
      setIsPlaying(!isPlaying);
    }
  };

  const handleSliderChange = (e) => {
    setIsPlaying(false);
    setCurrentStep(Number(e.target.value));
  };

  const handleSpeedChange = (e) => {
    setSpeed(Number(e.target.value));
  };

  // --- Render Logic ---
  const currentFrame = visualizationSteps[currentStep] || {};
  const {grid, visited, highlight, currentFarm, message, found} = currentFrame;

  const getCellClass = (r, c) => {
    const isLand = grid && grid[r][c] === 1;
    let classes = "w-16 h-16 border-2 flex items-center justify-center text-2xl font-bold transition-all duration-300";

    if (highlight && highlight.r === r && highlight.c === c) {
      if (highlight.type === "scan") classes += " bg-blue-400 border-blue-600 shadow-lg scale-110";
      else if (highlight.type === "found-start") classes += " bg-green-400 border-green-600 shadow-lg scale-110";
    } else if (currentFarm && r >= currentFarm.r1 && r <= currentFarm.r2 && c >= currentFarm.c1 && c <= currentFarm.c2) {
      classes += " bg-green-300 border-green-500";
    } else if (visited && visited[r][c]) {
      classes += " bg-gray-400 border-gray-500";
    } else {
      classes += isLand ? " bg-yellow-200 border-yellow-400" : " bg-sky-200 border-sky-400";
    }
    return classes;
  };

  const exampleGrids = {
    Simple: [
      [1, 0, 0],
      [0, 1, 1],
      [0, 1, 1],
    ],
    Complex: [
      [1, 1, 0, 0, 1],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 1, 1, 1],
      [1, 0, 1, 1, 1],
    ],
    "Single Row": [[1, 1, 1, 0, 1, 1]],
    "Single Col": [[1], [0], [1], [1]],
    "No Land": [
      [0, 0, 0],
      [0, 0, 0],
    ],
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4 font-sans">
      <div className="w-full max-w-5xl mx-auto bg-white rounded-xl shadow-2xl p-6">
        <header className="text-center mb-6">
          <h1 className="text-4xl font-bold text-gray-800">Find Farmland (LeetCode 1992)</h1>
          <p className="text-lg text-gray-600 mt-2">A step-by-step visualization of the algorithm.</p>
        </header>

        <div className="flex flex-col lg:flex-row gap-8">
          {/* Left Panel: Visualization */}
          <div className="flex-grow">
            <div className="flex justify-center items-center mb-4 gap-2">
              <span className="text-gray-600">Load Example:</span>
              {Object.entries(exampleGrids).map(([name, gridData]) => (
                <button
                  key={name}
                  onClick={() => setLand(gridData)}
                  className="px-3 py-1 bg-indigo-500 text-white rounded-md hover:bg-indigo-600 transition-colors"
                >
                  {name}
                </button>
              ))}
            </div>
            <div className="bg-gray-200 p-4 rounded-lg shadow-inner">
              {grid &&
                grid.map((row, r) => (
                  <div key={r} className="flex justify-center">
                    {row.map((_, c) => (
                      <div key={`${r}-${c}`} className={getCellClass(r, c)}>
                        {grid[r][c]}
                      </div>
                    ))}
                  </div>
                ))}
            </div>
          </div>

          {/* Right Panel: Controls & Info */}
          <div className="w-full lg:w-80 flex-shrink-0">
            <div className="bg-gray-50 p-4 rounded-lg shadow-md">
              <h2 className="text-xl font-semibold text-gray-700 mb-3">Controls</h2>
              <div className="flex items-center justify-center gap-2 mb-4">
                <button
                  onClick={handlePrevious}
                  disabled={currentStep === 0}
                  className="p-2 rounded-full bg-gray-200 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <polygon points="11 19 2 12 11 5 11 19"></polygon>
                    <polygon points="22 19 13 12 22 5 22 19"></polygon>
                  </svg>
                </button>
                <button onClick={handlePlayPause} className="p-3 rounded-full bg-blue-500 text-white hover:bg-blue-600 transition-colors shadow-md">
                  {isPlaying ? <PauseIcon /> : <PlayIcon />}
                </button>
                <button
                  onClick={handleNext}
                  disabled={currentStep === visualizationSteps.length - 1}
                  className="p-2 rounded-full bg-gray-200 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <polygon points="13 19 22 12 13 5 13 19"></polygon>
                    <polygon points="2 19 11 12 2 5 2 19"></polygon>
                  </svg>
                </button>
                <button onClick={handleReset} className="p-2 rounded-full bg-gray-200 hover:bg-gray-300 transition-colors">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <polyline points="23 4 23 10 17 10"></polyline>
                    <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>
                  </svg>
                </button>
              </div>
              <div className="mb-4">
                <label htmlFor="timeline" className="block text-sm font-medium text-gray-700 mb-1">
                  Timeline
                </label>
                <input
                  id="timeline"
                  type="range"
                  min="0"
                  max={visualizationSteps.length - 1}
                  value={currentStep}
                  onChange={handleSliderChange}
                  className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                />
                <div className="text-center text-sm text-gray-500 mt-1">
                  Step: {currentStep + 1} / {visualizationSteps.length}
                </div>
              </div>
              <div className="mb-4">
                <label htmlFor="speed" className="block text-sm font-medium text-gray-700 mb-1">
                  Speed
                </label>
                <input
                  id="speed"
                  type="range"
                  min="100"
                  max="1500"
                  step="100"
                  value={speed}
                  onChange={handleSpeedChange}
                  className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                />
              </div>
            </div>

            <div className="bg-blue-50 border-l-4 border-blue-500 text-blue-800 p-4 rounded-r-lg mt-4 shadow">
              <h3 className="font-bold">Current Action</h3>
              <p>{message || " "}</p>
            </div>

            <div className="mt-4 bg-green-50 p-4 rounded-lg shadow-md">
              <h3 className="text-lg font-semibold text-green-800 mb-2">Found Farmlands: {found ? found.length : 0}</h3>
              <div className="space-y-2 text-gray-700 font-mono">
                {found &&
                  found.map((farm, index) => (
                    <div key={index} className="bg-green-100 p-2 rounded">
                      [{farm.join(", ")}]
                    </div>
                  ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
