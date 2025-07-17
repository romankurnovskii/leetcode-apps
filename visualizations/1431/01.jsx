import React, {useState, useEffect, useMemo} from "react";

// --- Helper Components & Functions ---

const PlayIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
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

const PauseIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
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

const PrevIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
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
);

const NextIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
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
);

const ResetIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
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
);

// --- Main App Component ---

export default function KidsWithCandiesVisualizer() {
  // --- State Management ---
  const [candies, setCandies] = useState([2, 3, 5, 1, 3]);
  const [extraCandies, setExtraCandies] = useState(3);
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1000);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hover, setHover] = useState({prev: false, play: false, next: false, reset: false});

  // --- Algorithm & Visualization Logic ---

  const generateVisualization = useMemo(() => {
    return (candiesList, extra) => {
      const steps = [];
      const results = [];

      // Step 0: Initial state
      steps.push({type: "initial", candies: [...candiesList], extraCandies: extra, results: [], message: "Start with the list of kids' candies."});

      // Step 1: Find the maximum number of candies.
      let maxCandies = 0;
      if (candiesList.length > 0) {
        maxCandies = Math.max(...candiesList);
      }
      steps.push({
        type: "find_max",
        candies: [...candiesList],
        maxCandies,
        results: [],
        message: `First, find the greatest number of candies any kid has: ${maxCandies}.`,
      });

      // Step 2: Iterate through each kid and check if they can have the most candies.
      for (let i = 0; i < candiesList.length; i++) {
        const currentKidCandies = candiesList[i];
        const newTotal = currentKidCandies + extra;
        const canBeGreatest = newTotal >= maxCandies;

        // Show the calculation for the current kid
        steps.push({
          type: "check_kid",
          candies: [...candiesList],
          currentIndex: i,
          newTotal,
          maxCandies,
          canBeGreatest,
          results: [...results],
          message: `Checking kid ${i + 1}: ${currentKidCandies} + ${extra} = ${newTotal}.`,
        });

        results.push(canBeGreatest);

        // Show the result for the current kid being added to the list
        steps.push({
          type: "update_result",
          candies: [...candiesList],
          currentIndex: i,
          maxCandies,
          results: [...results],
          message: `Is ${newTotal} >= ${maxCandies}? ${canBeGreatest}. Adding to results.`,
        });
      }

      // Step 3: Final results
      steps.push({type: "final", candies: [...candiesList], results: [...results], message: "The process is complete. Here is the final result."});

      return {steps};
    };
  }, []);

  // --- Effects ---

  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth >= 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    const {steps} = generateVisualization(candies, extraCandies);
    setVisualizationSteps(steps);
    setCurrentStep(0);
    setIsPlaying(false);
  }, [candies, extraCandies, generateVisualization]);

  useEffect(() => {
    if (isPlaying) {
      const interval = setInterval(() => {
        setCurrentStep((prev) => (prev < visualizationSteps.length - 1 ? prev + 1 : (setIsPlaying(false), prev)));
      }, speed);
      return () => clearInterval(interval);
    }
  }, [isPlaying, speed, visualizationSteps.length]);

  // --- Event Handlers ---
  const handleNext = () => currentStep < visualizationSteps.length - 1 && setCurrentStep(currentStep + 1);
  const handlePrevious = () => currentStep > 0 && setCurrentStep(currentStep - 1);
  const handleReset = () => {
    setCurrentStep(0);
    setIsPlaying(false);
  };
  const handlePlayPause = () => (currentStep === visualizationSteps.length - 1 ? (setCurrentStep(0), setIsPlaying(true)) : setIsPlaying(!isPlaying));
  const handleSliderChange = (e) => {
    setIsPlaying(false);
    setCurrentStep(Number(e.target.value));
  };
  const handleHover = (key, isHovering) => setHover((prev) => ({...prev, [key]: isHovering}));
  const handleCandiesChange = (e) => {
    const list = e.target.value
      .split(",")
      .map((n) => parseInt(n.trim(), 10))
      .filter((n) => !isNaN(n));
    setCandies(list);
  };

  // --- Styles ---
  const styles = {
    container: {
      backgroundColor: "#f7f7f8",
      display: "flex",
      alignItems: "flex-start",
      justifyContent: "center",
      padding: "0.5rem",
      fontFamily: "sans-serif",
      minHeight: "100vh",
    },
    card: {width: "100%", maxWidth: "56rem", backgroundColor: "white", borderRadius: "0.5rem", border: "1px solid #e5e5e5", padding: "1rem"},
    mainGrid: {display: "flex", flexDirection: "column", gap: "1rem"},
    controlsPanel: {flex: 1},
    inputsContainer: {display: "flex", flexDirection: "column", gap: "0.75rem"},
    label: {fontSize: "0.875rem", fontWeight: "500", color: "#333"},
    input: {
      display: "block",
      width: "100%",
      boxSizing: "border-box",
      borderRadius: "0.375rem",
      border: "1px solid #ddd",
      padding: "0.5rem",
      fontFamily: "monospace",
      backgroundColor: "#fafafa",
    },
    controlsBox: {backgroundColor: "#f7f7f8", padding: "0.75rem", borderRadius: "0.5rem", marginTop: "1rem"},
    controlsHeader: {fontSize: "1rem", fontWeight: "600", color: "#333", marginBottom: "0.75rem", textAlign: "center"},
    buttonGroup: {display: "flex", alignItems: "center", justifyContent: "center", gap: "0.5rem", marginBottom: "0.75rem"},
    button: {
      padding: "0.4rem",
      borderRadius: "9999px",
      backgroundColor: "#e9e9ea",
      transition: "background-color 0.2s",
      border: "none",
      cursor: "pointer",
      display: "flex",
      alignItems: "center",
    },
    buttonHover: {backgroundColor: "#dcdce0"},
    playButton: {
      padding: "0.6rem",
      borderRadius: "9999px",
      backgroundColor: "#007aff",
      color: "white",
      border: "none",
      cursor: "pointer",
      display: "flex",
      alignItems: "center",
    },
    playButtonHover: {backgroundColor: "#005ecb"},
    disabledButton: {opacity: 0.5, cursor: "not-allowed"},
    sliderLabel: {display: "block", fontSize: "0.875rem", fontWeight: "500", color: "#333", marginBottom: "0.25rem"},
    slider: {width: "100%", height: "0.5rem", backgroundColor: "#e9e9ea", borderRadius: "0.5rem", appearance: "none", cursor: "pointer"},
    sliderSteps: {textAlign: "center", fontSize: "0.875rem", color: "#666", marginTop: "0.25rem"},
    vizPanel: {display: "flex", flexDirection: "column", gap: "1rem", flex: 2},
    vizBox: {
      backgroundColor: "#f7f7f8",
      padding: "1rem",
      borderRadius: "0.5rem",
      minHeight: "220px",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    },
    messageBox: {
      backgroundColor: "#f0f7ff",
      borderLeft: "3px solid #007aff",
      color: "#004085",
      padding: "0.75rem",
      borderRadius: "0 0.375rem 0.375rem 0",
    },
    messageTitle: {fontWeight: "600"},
    kidContainer: {display: "flex", gap: "0.75rem", flexWrap: "wrap", justifyContent: "center"},
    kid: {
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      gap: "0.25rem",
      padding: "0.5rem",
      borderRadius: "0.375rem",
      border: "2px solid transparent",
      transition: "all 0.3s",
    },
    kidCandies: {fontSize: "1.25rem", fontWeight: "bold"},
    kidLabel: {fontSize: "0.8rem", color: "#555"},
    resultBox: {padding: "0.5rem", borderRadius: "0.375rem", fontFamily: "monospace", fontSize: "1rem"},
    greenText: {color: "#28a745", fontWeight: "bold"},
    redText: {color: "#dc3545", fontWeight: "bold"},
  };

  // --- Render Logic ---
  const currentFrame = visualizationSteps[currentStep] || {};

  const renderFrame = () => {
    const {type, candies: frameCandies, maxCandies, currentIndex, newTotal, canBeGreatest, results} = currentFrame;

    const getKidStyle = (index) => {
      let style = {...styles.kid};
      if (type === "find_max" && frameCandies[index] === maxCandies) {
        style = {...style, borderColor: "#ffcc00", backgroundColor: "#fffbe6"};
      }
      if ((type === "check_kid" || type === "update_result") && index === currentIndex) {
        style = {...style, borderColor: "#007aff", backgroundColor: "#f0f7ff", transform: "scale(1.1)"};
      }
      return style;
    };

    return (
      <div style={{width: "100%", display: "flex", flexDirection: "column", alignItems: "center", gap: "1rem"}}>
        <div style={styles.kidContainer}>
          {frameCandies &&
            frameCandies.map((candyCount, i) => (
              <div key={i} style={getKidStyle(i)}>
                <span style={styles.kidCandies}>{candyCount}</span>
                <span style={styles.kidLabel}>Kid {i + 1}</span>
              </div>
            ))}
        </div>

        {type === "find_max" && (
          <div style={{textAlign: "center", fontSize: "1.125rem"}}>
            Max Candies: <span style={{...styles.kidCandies, color: "#ff9500"}}>{maxCandies}</span>
          </div>
        )}

        {(type === "check_kid" || type === "update_result") && (
          <div style={{textAlign: "center", fontSize: "1.125rem"}}>
            {newTotal}{" "}
            <span style={{color: canBeGreatest ? styles.greenText.color : styles.redText.color, fontWeight: "bold"}}>
              {canBeGreatest ? "≥" : "<"}
            </span>{" "}
            {maxCandies}
          </div>
        )}

        {results && results.length > 0 && (
          <div style={{textAlign: "center", display: "flex", gap: "0.5rem", flexWrap: "wrap", justifyContent: "center"}}>
            <span style={{alignSelf: "center", fontSize: "0.875rem", color: "#555"}}>Results:</span>
            {results.map((res, i) => (
              <span
                key={i}
                style={{
                  ...styles.resultBox,
                  backgroundColor: res ? "#eaf8f0" : "#fdecea",
                  color: res ? styles.greenText.color : styles.redText.color,
                }}
              >
                {res.toString()}
              </span>
            ))}
          </div>
        )}
      </div>
    );
  };

  // --- Component JSX ---
  const prevButtonStyle = {...styles.button, ...(hover.prev && styles.buttonHover), ...(currentStep === 0 && styles.disabledButton)};
  const nextButtonStyle = {
    ...styles.button,
    ...(hover.next && styles.buttonHover),
    ...(currentStep >= visualizationSteps.length - 1 && styles.disabledButton),
  };
  const playButtonStyle = {...styles.playButton, ...(hover.play && styles.playButtonHover)};
  const resetButtonStyle = {...styles.button, ...(hover.reset && styles.buttonHover)};
  const mainGridStyle = {...styles.mainGrid, ...(isDesktop && {flexDirection: "row"})};

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={mainGridStyle}>
          <div style={styles.controlsPanel}>
            <div style={styles.inputsContainer}>
              <div>
                <label htmlFor="candies" style={styles.label}>
                  Candies (comma-separated)
                </label>
                <input type="text" id="candies" value={candies.join(", ")} onChange={handleCandiesChange} style={styles.input} />
              </div>
              <div>
                <label htmlFor="extraCandies" style={styles.label}>
                  Extra Candies
                </label>
                <input
                  type="number"
                  id="extraCandies"
                  value={extraCandies}
                  onChange={(e) => setExtraCandies(Number(e.target.value))}
                  style={styles.input}
                />
              </div>
            </div>
            <div style={styles.controlsBox}>
              <h2 style={styles.controlsHeader}>Controls</h2>
              <div style={styles.buttonGroup}>
                <button
                  onClick={handlePrevious}
                  disabled={currentStep === 0}
                  style={prevButtonStyle}
                  onMouseEnter={() => handleHover("prev", true)}
                  onMouseLeave={() => handleHover("prev", false)}
                >
                  <PrevIcon />
                </button>
                <button
                  onClick={handlePlayPause}
                  style={playButtonStyle}
                  onMouseEnter={() => handleHover("play", true)}
                  onMouseLeave={() => handleHover("play", false)}
                >
                  {isPlaying ? <PauseIcon /> : <PlayIcon />}
                </button>
                <button
                  onClick={handleNext}
                  disabled={currentStep >= visualizationSteps.length - 1}
                  style={nextButtonStyle}
                  onMouseEnter={() => handleHover("next", true)}
                  onMouseLeave={() => handleHover("next", false)}
                >
                  <NextIcon />
                </button>
                <button
                  onClick={handleReset}
                  style={resetButtonStyle}
                  onMouseEnter={() => handleHover("reset", true)}
                  onMouseLeave={() => handleHover("reset", false)}
                >
                  <ResetIcon />
                </button>
              </div>
              <div>
                <label htmlFor="timeline" style={styles.sliderLabel}>
                  Timeline
                </label>
                <input
                  id="timeline"
                  type="range"
                  min="0"
                  max={visualizationSteps.length - 1}
                  value={currentStep}
                  onChange={handleSliderChange}
                  style={styles.slider}
                />
                <div style={styles.sliderSteps}>
                  Step: {currentStep + 1} / {visualizationSteps.length}
                </div>
              </div>
            </div>
          </div>

          <div style={styles.vizPanel}>
            <div style={styles.vizBox}>{renderFrame()}</div>
            <div style={styles.messageBox}>
              <h3 style={styles.messageTitle}>Current Action</h3>
              <p>{(currentFrame && currentFrame.message) || " "}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
