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

// Euclidean algorithm for GCD
const gcd = (a, b) => {
  if (b === 0) return a;
  return gcd(b, a % b);
};

// --- Main App Component ---

export default function GcdOfStringsVisualizer() {
  // --- State Management ---
  const [str1, setStr1] = useState("ABCABC");
  const [str2, setStr2] = useState("ABC");
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1000);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);

  // State to manage hover effects for buttons since we can't use :hover with inline styles
  const [hover, setHover] = useState({prev: false, play: false, next: false, reset: false});

  // --- Algorithm & Visualization Logic ---

  const generateVisualization = useMemo(() => {
    return (s1, s2) => {
      const steps = [];
      // Step 0: Initial state
      steps.push({type: "initial", s1, s2, message: "Starting with the two input strings."});

      // Step 1: The core property check for string divisibility.
      // If two strings `s1` and `s2` share a common divisor string `x`,
      // then `s1 + s2` must equal `s2 + s1`.
      const concat1 = s1 + s2;
      const concat2 = s2 + s1;
      const areDivisible = concat1 === concat2;
      steps.push({type: "concat_check", s1, s2, concat1, concat2, areDivisible, message: "Check if str1 + str2 == str2 + str1."});

      // If the concatenation check fails, no common divisor can exist.
      if (!areDivisible) {
        steps.push({type: "final", result: "", message: "Concatenations are not equal; no common divisor exists."});
        return {steps, result: ""};
      }

      // Step 2: If a common divisor exists, its length must be a common divisor
      // of the lengths of `s1` and `s2`. The largest possible divisor string will
      // have a length equal to the GCD of the original string lengths.
      const len1 = s1.length;
      const len2 = s2.length;
      steps.push({type: "gcd_intro", len1, len2, message: `Find GCD of lengths: ${len1} and ${len2}.`});

      // Use the Euclidean algorithm to find the GCD of the lengths.
      let a = len1,
        b = len2;
      while (b !== 0) {
        steps.push({type: "gcd_step", a, b, remainder: a % b, message: `Calculating GCD(${a}, ${b}).`});
        [a, b] = [b, a % b];
      }
      steps.push({type: "gcd_result", gcd: a, message: `The GCD of the lengths is ${a}.`});

      // Step 3: The result is the prefix of one of the strings with the calculated GCD length.
      const gcdLen = a;
      const finalResult = s1.substring(0, gcdLen);
      steps.push({type: "substring", s1, gcdLen, result: finalResult, message: `The result is the prefix of str1 with length ${gcdLen}.`});

      // Step 4: Final verification step.
      steps.push({
        type: "final",
        s1,
        s2,
        result: finalResult,
        isVerified: finalResult && finalResult.repeat(s1.length / gcdLen) === s1 && finalResult.repeat(s2.length / gcdLen) === s2,
        message: "Verification complete.",
      });

      return {steps, result: finalResult};
    };
  }, []);

  // --- Effects ---

  // Effect to handle responsive layout changes
  useEffect(() => {
    const handleResize = () => {
      setIsDesktop(window.innerWidth >= 768);
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    const {steps} = generateVisualization(str1, str2);
    setVisualizationSteps(steps);
    setCurrentStep(0);
    setIsPlaying(false);
  }, [str1, str2, generateVisualization]);

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

  // --- Styles (Optimized for smaller screens) ---
  const styles = {
    container: {
      minHeight: "100vh",
      backgroundColor: "#f3f4f6",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      padding: "0.5rem",
      fontFamily: "sans-serif",
    },
    card: {
      width: "100%",
      maxWidth: "56rem",
      backgroundColor: "white",
      borderRadius: "0.75rem",
      boxShadow: "0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)",
      padding: "1rem",
    },
    mainGrid: {display: "flex", flexDirection: "column", gap: "1.5rem"},
    controlsPanel: {display: "flex", flexDirection: "column", gap: "1rem", flex: 1},
    inputsContainer: {display: "flex", flexDirection: "column", gap: "0.75rem"},
    label: {display: "block", fontSize: "0.875rem", fontWeight: "500", color: "#374151"},
    input: {
      marginTop: "0.25rem",
      display: "block",
      width: "100%",
      boxSizing: "border-box",
      borderRadius: "0.375rem",
      border: "1px solid #d1d5db",
      boxShadow: "0 1px 2px 0 rgb(0 0 0 / 0.05)",
      padding: "0.5rem",
      fontFamily: "monospace",
    },
    controlsBox: {
      backgroundColor: "#f9fafb",
      padding: "0.75rem",
      borderRadius: "0.5rem",
      boxShadow: "0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)",
      marginTop: "1rem",
    },
    controlsHeader: {fontSize: "1.125rem", fontWeight: "600", color: "#374151", marginBottom: "0.75rem", textAlign: "center"},
    buttonGroup: {display: "flex", alignItems: "center", justifyContent: "center", gap: "0.5rem", marginBottom: "0.75rem"},
    button: {
      padding: "0.4rem",
      borderRadius: "9999px",
      backgroundColor: "#e5e7eb",
      transition: "background-color 0.2s",
      border: "none",
      cursor: "pointer",
      display: "flex",
      alignItems: "center",
    },
    buttonHover: {backgroundColor: "#d1d5db"},
    playButton: {
      padding: "0.6rem",
      borderRadius: "9999px",
      backgroundColor: "#3b82f6",
      color: "white",
      boxShadow: "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)",
      border: "none",
      cursor: "pointer",
      display: "flex",
      alignItems: "center",
    },
    playButtonHover: {backgroundColor: "#2563eb"},
    disabledButton: {opacity: 0.5, cursor: "not-allowed"},
    sliderLabel: {display: "block", fontSize: "0.875rem", fontWeight: "500", color: "#374151", marginBottom: "0.25rem"},
    slider: {width: "100%", height: "0.5rem", backgroundColor: "#e5e7eb", borderRadius: "0.5rem", appearance: "none", cursor: "pointer"},
    sliderSteps: {textAlign: "center", fontSize: "0.875rem", color: "#6b7280", marginTop: "0.25rem"},
    vizPanel: {display: "flex", flexDirection: "column", gap: "1rem", flex: 2},
    vizBox: {
      backgroundColor: "#e5e7eb",
      padding: "1rem",
      borderRadius: "0.5rem",
      boxShadow: "inset 0 2px 4px 0 rgb(0 0 0 / 0.05)",
      minHeight: "250px",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    },
    messageBox: {
      backgroundColor: "#eff6ff",
      borderLeft: "4px solid #3b82f6",
      color: "#1e40af",
      padding: "1rem",
      borderRadius: "0 0.5rem 0.5rem 0",
      boxShadow: "0 1px 2px 0 rgb(0 0 0 / 0.05)",
      minHeight: "60px",
    },
    messageTitle: {fontWeight: "bold"},
    stringBox: {
      fontSize: "1.125rem",
      fontFamily: "monospace",
      padding: "0.5rem",
      borderRadius: "0.375rem",
      letterSpacing: "0.05em",
      wordBreak: "break-all",
    },
    greenText: {color: "#166534", fontWeight: "bold"},
    redText: {color: "#991b1b", fontWeight: "bold"},
    finalResultBox: {textAlign: "center", padding: "1rem", backgroundColor: "#f0fdf4", borderRadius: "0.5rem", width: "100%"},
    finalResultText: {
      fontSize: "1.875rem",
      fontFamily: "monospace",
      padding: "0.75rem",
      backgroundColor: "white",
      borderRadius: "0.5rem",
      boxShadow: "inset 0 2px 4px 0 rgb(0 0 0 / 0.05)",
      letterSpacing: "0.05em",
      wordBreak: "break-all",
    },
    gcdCalcBox: {textAlign: "center", padding: "1rem", backgroundColor: "#f9fafb", borderRadius: "0.5rem", width: "100%"},
  };

  // --- Render Logic ---
  const currentFrame = visualizationSteps[currentStep] || {};

  const renderFrame = () => {
    switch (currentFrame.type) {
      case "initial":
      case "concat_check":
        return (
          <div style={{textAlign: "center", display: "flex", flexDirection: "column", gap: "1rem", width: "100%"}}>
            <div>
              <p style={{fontSize: "1rem", fontWeight: "500", color: "#4b5563"}}>str1</p>
              <p style={{...styles.stringBox, backgroundColor: "#dbeafe"}}>{currentFrame.s1}</p>
            </div>
            <div>
              <p style={{fontSize: "1rem", fontWeight: "500", color: "#4b5563"}}>str2</p>
              <p style={{...styles.stringBox, backgroundColor: "#e0e7ff"}}>{currentFrame.s2}</p>
            </div>
            {currentFrame.type === "concat_check" && (
              <div style={{paddingTop: "1rem", display: "flex", flexDirection: "column", gap: "0.5rem"}}>
                <p style={{...styles.stringBox, fontSize: "1rem", backgroundColor: "#f3f4f6"}}>{currentFrame.concat1}</p>
                <p style={{...styles.stringBox, fontSize: "1rem", backgroundColor: "#f3f4f6"}}>{currentFrame.concat2}</p>
                <p
                  style={{
                    fontSize: "1.25rem",
                    fontWeight: "bold",
                    paddingTop: "0.5rem",
                    ...(currentFrame.areDivisible ? styles.greenText : styles.redText),
                  }}
                >
                  {currentFrame.areDivisible ? "EQUAL ✓" : "NOT EQUAL ✗"}
                </p>
              </div>
            )}
          </div>
        );
      case "gcd_intro":
      case "gcd_step":
      case "gcd_result":
        return (
          <div style={styles.gcdCalcBox}>
            <h3 style={{fontSize: "1.25rem", fontWeight: "bold", color: "#374151"}}>GCD Calculation</h3>
            {currentFrame.type === "gcd_intro" && (
              <p style={{fontSize: "1.875rem", fontFamily: "monospace"}}>
                GCD({currentFrame.len1}, {currentFrame.len2})
              </p>
            )}
            {currentFrame.type === "gcd_step" && (
              <div style={{fontFamily: "monospace", fontSize: "1.25rem", display: "flex", flexDirection: "column", gap: "0.5rem"}}>
                <p>
                  GCD(<span style={{color: "#2563eb"}}>{currentFrame.a}</span>, <span style={{color: "#7c3aed"}}>{currentFrame.b}</span>)
                </p>
                <p style={{fontSize: "1.125rem"}}>
                  {currentFrame.a} % {currentFrame.b} = <span style={{color: "#be123c"}}>{currentFrame.remainder}</span>
                </p>
                <p style={{fontSize: "1.125rem"}}>
                  Next: GCD({currentFrame.b}, {currentFrame.remainder})
                </p>
              </div>
            )}
            {currentFrame.type === "gcd_result" && (
              <p style={{fontSize: "1.875rem", fontFamily: "monospace"}}>
                Result: <span style={{color: "#16a34a", fontWeight: "bold"}}>{currentFrame.gcd}</span>
              </p>
            )}
          </div>
        );
      case "substring":
        return (
          <div style={{textAlign: "center", display: "flex", flexDirection: "column", gap: "1rem"}}>
            <p style={{fontSize: "1rem", fontWeight: "500", color: "#4b5563"}}>str1.substring(0, {currentFrame.gcdLen})</p>
            <p style={{...styles.stringBox, fontSize: "1.5rem", backgroundColor: "#fefce8"}}>
              <span style={{backgroundColor: "#facc15", padding: "0.25rem", borderRadius: "0.25rem"}}>{currentFrame.result}</span>
              <span>{currentFrame.s1.substring(currentFrame.gcdLen)}</span>
            </p>
          </div>
        );
      case "final":
        return (
          <div style={styles.finalResultBox}>
            <h3 style={{fontSize: "1.25rem", fontWeight: "bold", color: "#374151"}}>Final Result</h3>
            <p style={styles.finalResultText}>{currentFrame.result ? `"${currentFrame.result}"` : '""'}</p>
            {currentFrame.isVerified && (
              <div style={{fontSize: "1rem", paddingTop: "1rem"}}>
                <p>
                  ✅ <span style={{fontWeight: "bold", color: "#15803d"}}>{currentFrame.result}</span> x{" "}
                  {currentFrame.s1.length / currentFrame.result.length} = {currentFrame.s1}
                </p>
                <p>
                  ✅ <span style={{fontWeight: "bold", color: "#15803d"}}>{currentFrame.result}</span> x{" "}
                  {currentFrame.s2.length / currentFrame.result.length} = {currentFrame.s2}
                </p>
              </div>
            )}
          </div>
        );
      default:
        return <p>{currentFrame.message || "Select an action"}</p>;
    }
  };

  // Combine base and hover styles for buttons
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
          {/* Left Panel */}
          <div style={styles.controlsPanel}>
            <div style={styles.inputsContainer}>
              <div>
                <label htmlFor="str1" style={styles.label}>
                  String 1
                </label>
                <input type="text" id="str1" value={str1} onChange={(e) => setStr1(e.target.value)} style={styles.input} />
              </div>
              <div>
                <label htmlFor="str2" style={styles.label}>
                  String 2
                </label>
                <input type="text" id="str2" value={str2} onChange={(e) => setStr2(e.target.value)} style={styles.input} />
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

          {/* Right Panel */}
          <div style={styles.vizPanel}>
            <div style={styles.vizBox}>{renderFrame()}</div>
            <div style={styles.messageBox}>
              <h3 style={styles.messageTitle}>Current Action</h3>
              <p>{currentFrame.message || " "}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
