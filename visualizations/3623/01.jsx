import React, {useState, useMemo, useEffect, useRef} from "react";

// SVG Icon Components
const PlayIcon = ({color}) => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M8 5V19L19 12L8 5Z" fill={color} />
  </svg>
);

const PauseIcon = ({color}) => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M6 19H10V5H6V19ZM14 5V19H18V5H14Z" fill={color} />
  </svg>
);

const PrevIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M15.41 7.41L14 6L8 12L14 18L15.41 16.59L10.83 12L15.41 7.41Z" fill="currentColor" />
    <path d="M7 6H9V18H7V6Z" fill="currentColor" />
  </svg>
);

const NextIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M8.59 16.59L10 18L16 12L10 6L8.59 7.41L13.17 12L8.59 16.59Z" fill="currentColor" />
    <path d="M15 6H17V18H15V6Z" fill="currentColor" />
  </svg>
);

const ResetIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path
      d="M12 5V1L7 6L12 11V7C15.31 7 18 9.69 18 13C18 16.31 15.31 19 12 19C8.69 19 6 16.31 6 13H4C4 17.42 7.58 21 12 21C16.42 21 20 17.42 20 13C20 8.58 16.42 5 12 5Z"
      fill="currentColor"
    />
  </svg>
);

const MOD = 10 ** 9 + 7;

// Main Visualizer Component
const CountTrapezoidsIVisualizer = () => {
  const [pointsInput, setPointsInput] = useState("[[1,0],[2,0],[3,0],[2,2],[3,2]]");
  const [parsedPoints, setParsedPoints] = useState([
    [1, 0],
    [2, 0],
    [3, 0],
    [2, 2],
    [3, 2],
  ]);
  const [error, setError] = useState("");

  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth > 768);
  const [hoveredButton, setHoveredButton] = useState(null);

  const intervalRef = useRef(null);

  const generateVisualization = (points) => {
    if (!points || points.length < 4) {
      setError("Input must be an array of at least 4 points.");
      return [];
    }
    const steps = [];

    // Step 0: Initial state
    steps.push({
      message: "Start with the initial set of points.",
      pointsToGroup: [...points],
      y_groups: {},
      pairs: [],
      calculation: null,
      highlightedY: null,
      stage: "grouping",
    });

    // Step 1: Grouping by Y
    const y_groups = {};
    const localPointsToGroup = [...points];

    while (localPointsToGroup.length > 0) {
      const point = localPointsToGroup.shift();
      const y = point[1];
      if (!y_groups[y]) y_groups[y] = [];
      y_groups[y].push(point);

      steps.push({
        message: `Grouping point [${point.join(", ")}] by its y-coordinate.`,
        pointsToGroup: [...localPointsToGroup],
        y_groups: JSON.parse(JSON.stringify(y_groups)),
        highlightedPoint: point,
        pairs: [],
        calculation: null,
        highlightedY: y,
        stage: "grouping",
      });
    }

    steps.push({
      message: "All points have been grouped by their y-coordinate.",
      y_groups,
      pairs: [],
      calculation: null,
      highlightedY: null,
      stage: "calculating_pairs",
    });

    // Step 2: Calculate Pairs C(c, 2)
    const pairs = [];
    const sortedYLevels = Object.keys(y_groups)
      .map(Number)
      .sort((a, b) => a - b);

    for (const y of sortedYLevels) {
      const c = y_groups[y].length;
      steps.push({
        message: `Checking group at y=${y}, which has ${c} points.`,
        y_groups,
        pairs: [...pairs],
        calculation: null,
        highlightedY: y,
        stage: "calculating_pairs",
      });

      if (c >= 2) {
        const numPairs = (c * (c - 1)) / 2;
        pairs.push(numPairs);
        steps.push({
          message: `With ${c} points, we can form C(${c}, 2) = ${numPairs} horizontal segments.`,
          y_groups,
          pairs: [...pairs],
          calculation: {text: `C(${c}, 2) = ${numPairs}`, target: "pairs"},
          highlightedY: y,
          stage: "calculating_pairs",
        });
      } else {
        steps.push({
          message: `Skipping y=${y} as it has fewer than 2 points.`,
          y_groups,
          pairs: [...pairs],
          calculation: null,
          highlightedY: y,
          stage: "calculating_pairs",
        });
      }
    }

    steps.push({
      message: "Finished calculating horizontal segments for each y-level.",
      y_groups,
      pairs: [...pairs],
      calculation: null,
      highlightedY: null,
      stage: "final_calculation",
    });

    // Step 3: Final Calculation
    const total_sum = pairs.reduce((acc, x) => acc + x, 0);
    steps.push({
      message: "Calculate total_sum = sum of all values in the pairs list.",
      y_groups,
      pairs,
      calculation: {text: `Total Sum = ${pairs.join(" + ") || 0} = ${total_sum}`, target: "total_sum"},
      highlightedY: null,
      total_sum,
      stage: "final_calculation",
    });

    const sum_of_squares = pairs.reduce((acc, x) => acc + x * x, 0);
    steps.push({
      message: "Calculate sum_of_squares = sum of the square of each value.",
      y_groups,
      pairs,
      calculation: {text: `Sum of Squares = ${pairs.map((p) => `${p}²`).join(" + ") || 0} = ${sum_of_squares}`, target: "sum_of_squares"},
      total_sum,
      sum_of_squares,
      stage: "final_calculation",
    });

    const res = (BigInt(total_sum) * BigInt(total_sum) - BigInt(sum_of_squares)) / BigInt(2);
    const finalResult = Number(res % BigInt(MOD));

    steps.push({
      message: "Apply the formula: (total_sum² - sum_of_squares) / 2.",
      y_groups,
      pairs,
      calculation: {text: `Result = (${total_sum}² - ${sum_of_squares}) / 2 = ${finalResult}`, target: "result"},
      total_sum,
      sum_of_squares,
      result: finalResult,
      stage: "final_calculation",
    });

    steps.push({
      message: `The total number of horizontal trapezoids is ${finalResult}.`,
      y_groups,
      pairs,
      total_sum,
      sum_of_squares,
      result: finalResult,
      stage: "done",
      isFinal: true,
    });

    return steps;
  };

  useMemo(() => {
    try {
      const parsed = JSON.parse(pointsInput);
      if (Array.isArray(parsed) && parsed.every((p) => Array.isArray(p) && p.length === 2 && typeof p[0] === "number" && typeof p[1] === "number")) {
        setParsedPoints(parsed);
        setError("");
      } else {
        setError("Invalid input format. Use e.g., [[1,0],[2,0]].");
      }
    } catch (e) {
      setError("Invalid JSON format.");
    }
  }, [pointsInput]);

  useEffect(() => {
    setVisualizationSteps(generateVisualization(parsedPoints));
    setCurrentStep(0);
    setIsPlaying(false);
  }, [parsedPoints]);

  useEffect(() => {
    if (isPlaying && currentStep < visualizationSteps.length - 1) {
      intervalRef.current = setTimeout(() => {
        setCurrentStep((prev) => prev + 1);
      }, 1500 / speed);
    } else if (currentStep === visualizationSteps.length - 1) {
      setIsPlaying(false);
    }
    return () => clearTimeout(intervalRef.current);
  }, [isPlaying, currentStep, speed, visualizationSteps.length]);

  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth > 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const handlePlayPause = () => {
    if (isPlaying) {
      setIsPlaying(false);
    } else {
      if (currentStep === visualizationSteps.length - 1) {
        setCurrentStep(0);
      }
      setIsPlaying(true);
    }
  };

  const handleReset = () => {
    setCurrentStep(0);
    setIsPlaying(false);
  };

  const handleNext = () => {
    setIsPlaying(false);
    if (currentStep < visualizationSteps.length - 1) {
      setCurrentStep((prev) => prev + 1);
    }
  };

  const handlePrev = () => {
    setIsPlaying(false);
    if (currentStep > 0) {
      setCurrentStep((prev) => prev - 1);
    }
  };

  const currentStepData = visualizationSteps[currentStep] || {};
  const {message, pointsToGroup, y_groups, pairs, calculation, highlightedY, highlightedPoint, total_sum, sum_of_squares, result, stage, isFinal} =
    currentStepData;

  // Styling
  const styles = {
    container: {
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
      display: "flex",
      justifyContent: "center",
      padding: "2rem 1rem",
    },
    card: {
      backgroundColor: "white",
      borderRadius: "12px",
      boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)",
      padding: isDesktop ? "1.5rem" : "1rem",
      width: "100%",
      maxWidth: "900px",
      display: "flex",
      flexDirection: isDesktop ? "row" : "column",
      gap: "1rem",
    },
    leftPanel: {
      flex: "1",
      display: "flex",
      flexDirection: "column",
      gap: "1rem",
    },
    rightPanel: {
      flex: "2",
      display: "flex",
      flexDirection: "column",
      gap: "1rem",
    },
    inputSection: {display: "flex", flexDirection: "column", gap: "0.5rem"},
    label: {fontWeight: "600", color: "#333", fontSize: "0.9rem"},
    textarea: {
      minHeight: "80px",
      padding: "0.5rem",
      borderRadius: "6px",
      border: `1px solid ${error ? "#e53e3e" : "#e5e5e5"}`,
      fontFamily: "monospace",
      fontSize: "0.9rem",
      resize: "vertical",
    },
    error: {color: "#e53e3e", fontSize: "0.8rem"},
    controls: {
      display: "flex",
      flexDirection: "column",
      gap: "0.75rem",
      padding: "0.75rem",
      borderRadius: "8px",
      border: "1px solid #e5e5e5",
    },
    buttonGroup: {display: "flex", justifyContent: "space-between", alignItems: "center"},
    button: (isHovered) => ({
      background: isHovered ? "#e9e9eb" : "transparent",
      border: "none",
      borderRadius: "6px",
      padding: "0.5rem",
      cursor: "pointer",
      color: "#333",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    }),
    playButton: (isHovered) => ({
      background: isHovered ? "#0066d6" : "#007aff",
      border: "none",
      borderRadius: "6px",
      padding: "0.5rem",
      cursor: "pointer",
      color: "white",
      flexGrow: "1",
      margin: "0 0.5rem",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    }),
    sliderContainer: {display: "flex", alignItems: "center", gap: "0.5rem", fontSize: "0.8rem"},
    slider: {width: "100%"},
    stepCounter: {
      textAlign: "center",
      fontSize: "0.8rem",
      color: "#666",
      margin: "0.25rem 0",
    },
    visualizationArea: {
      border: "1px solid #e5e5e5",
      borderRadius: "8px",
      padding: "0.75rem",
      minHeight: "250px",
      display: "flex",
      flexDirection: "column",
      gap: "1rem",
    },
    messageBox: {
      backgroundColor: "#f0f4ff",
      border: "1px solid #cce5ff",
      borderRadius: "6px",
      padding: "0.25rem 0.75rem",
      color: "#004085",
      fontSize: "0.75rem",
      textAlign: "center",
      minHeight: "2.5rem",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    },
    point: (isHighlighted) => ({
      display: "inline-block",
      padding: "0.2rem 0.4rem",
      margin: "0.2rem",
      backgroundColor: "#e9e9eb",
      border: `2px solid ${isHighlighted ? "#007aff" : "#d1d1d6"}`,
      borderRadius: "4px",
      fontFamily: "monospace",
      fontSize: "0.8rem",
      transition: "all 0.3s ease",
      transform: isHighlighted ? "scale(1.15)" : "scale(1)",
    }),
    yGroupRow: (isHighlighted) => ({
      display: "flex",
      alignItems: "center",
      gap: "0.5rem",
      padding: "0.5rem",
      borderRadius: "6px",
      border: `2px solid ${isHighlighted ? "#007aff" : "transparent"}`,
      backgroundColor: isHighlighted ? "#f0f4ff" : "transparent",
      transition: "all 0.3s ease",
    }),
    yGroupLabel: {
      fontFamily: "monospace",
      fontWeight: "bold",
      color: "#555",
      minWidth: "50px",
    },
    dataStructureView: {
      display: "flex",
      flexDirection: isDesktop ? "row" : "column",
      gap: "1rem",
      flexWrap: "wrap",
    },
    dataBox: (isHighlighted) => ({
      flex: 1,
      minWidth: "150px",
      padding: "0.75rem",
      border: `1px solid ${isHighlighted ? "#007aff" : "#e5e5e5"}`,
      borderRadius: "6px",
      backgroundColor: isHighlighted ? "#f0f4ff" : "#fcfcfd",
    }),
    dataTitle: {fontSize: "0.75rem", fontWeight: "600", color: "#666", marginBottom: "0.5rem", textTransform: "uppercase"},
    pairsList: {display: "flex", gap: "0.3rem", flexWrap: "wrap"},
    pairItem: {padding: "0.2rem 0.4rem", backgroundColor: "#e9e9eb", borderRadius: "4px", fontSize: "0.8rem"},
    calculationText: {
      fontFamily: "monospace",
      fontSize: "0.9rem",
      color: "#007aff",
      marginTop: "0.5rem",
      wordBreak: "break-all",
    },
  };

  const sortedYGroups = y_groups
    ? Object.keys(y_groups)
        .map(Number)
        .sort((a, b) => a - b)
    : [];

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.leftPanel}>
          <div style={styles.inputSection}>
            <label htmlFor="points-input" style={styles.label}>
              Points Input
            </label>
            <textarea id="points-input" style={styles.textarea} value={pointsInput} onChange={(e) => setPointsInput(e.target.value)} />
            {error && <p style={styles.error}>{error}</p>}
          </div>
          <div style={styles.controls}>
            <div style={styles.buttonGroup}>
              <button
                style={styles.button(hoveredButton === "prev")}
                onClick={handlePrev}
                onMouseEnter={() => setHoveredButton("prev")}
                onMouseLeave={() => setHoveredButton(null)}
              >
                <PrevIcon />
              </button>
              <button
                style={styles.playButton(hoveredButton === "play")}
                onClick={handlePlayPause}
                onMouseEnter={() => setHoveredButton("play")}
                onMouseLeave={() => setHoveredButton(null)}
              >
                {isPlaying ? <PauseIcon color="white" /> : <PlayIcon color="white" />}
              </button>
              <button
                style={styles.button(hoveredButton === "next")}
                onClick={handleNext}
                onMouseEnter={() => setHoveredButton("next")}
                onMouseLeave={() => setHoveredButton(null)}
              >
                <NextIcon />
              </button>
              <button
                style={styles.button(hoveredButton === "reset")}
                onClick={handleReset}
                onMouseEnter={() => setHoveredButton("reset")}
                onMouseLeave={() => setHoveredButton(null)}
              >
                <ResetIcon />
              </button>
            </div>
            <div style={styles.sliderContainer}>
              <span>1x</span>
              <input
                type="range"
                min="0.5"
                max="4"
                step="0.1"
                value={speed}
                onChange={(e) => setSpeed(parseFloat(e.target.value))}
                style={styles.slider}
              />
              <span>4x</span>
            </div>
            <div style={styles.stepCounter}>{visualizationSteps.length > 0 ? `Step ${currentStep + 1} of ${visualizationSteps.length}` : " "}</div>
            <input
              type="range"
              min="0"
              max={visualizationSteps.length > 0 ? visualizationSteps.length - 1 : 0}
              value={currentStep}
              onChange={(e) => {
                setIsPlaying(false);
                setCurrentStep(parseInt(e.target.value));
              }}
              style={styles.slider}
            />
          </div>
        </div>

        <div style={styles.rightPanel}>
          <div style={styles.messageBox}>
            <p>{message || " "}</p>
          </div>
          <div style={styles.visualizationArea}>
            {stage === "grouping" && (
              <div>
                <div style={styles.dataTitle}>Points to Group</div>
                <div>
                  {pointsToGroup?.map((p, i) => (
                    <span key={i} style={styles.point(p === highlightedPoint)}>
                      [{p.join(",")}]
                    </span>
                  ))}
                </div>
              </div>
            )}

            <div style={{...styles.dataTitle, marginTop: stage === "grouping" ? "1rem" : "0"}}>Y-Groups</div>
            <div>
              {y_groups &&
                sortedYGroups.map((y) => (
                  <div key={y} style={styles.yGroupRow(y === highlightedY)}>
                    <div style={styles.yGroupLabel}>y={y}:</div>
                    <div>
                      {y_groups[y].map((p, i) => (
                        <span key={i} style={styles.point(p === highlightedPoint)}>
                          [{p.join(",")}]
                        </span>
                      ))}
                    </div>
                  </div>
                ))}
            </div>

            <div style={styles.dataStructureView}>
              <div style={styles.dataBox(calculation?.target === "pairs")}>
                <div style={styles.dataTitle}>Pairs C(c,2)</div>
                <div style={styles.pairsList}>
                  {pairs?.map((p, i) => (
                    <span key={i} style={styles.pairItem}>
                      {p}
                    </span>
                  ))}
                </div>
                {calculation?.target === "pairs" && <p style={styles.calculationText}>{calculation.text}</p>}
              </div>
              <div style={{flex: 2, display: "flex", flexDirection: "column", gap: "0.5rem"}}>
                <div
                  style={styles.dataBox(
                    calculation?.target === "total_sum" || calculation?.target === "sum_of_squares" || calculation?.target === "result"
                  )}
                >
                  <div style={styles.dataTitle}>Formula</div>
                  <div>total_sum: {total_sum ?? "..."}</div>
                  <div>sum_of_squares: {sum_of_squares ?? "..."}</div>
                  <div style={{fontWeight: "bold"}}>Result: {isFinal ? <span style={{color: "#28a745"}}>{result}</span> : result ?? "..."}</div>
                  {(calculation?.target === "total_sum" || calculation?.target === "sum_of_squares" || calculation?.target === "result") && (
                    <p style={styles.calculationText}>{calculation.text}</p>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CountTrapezoidsIVisualizer;
