import React, {useState, useMemo, useEffect, useCallback} from "react";

// --- SVG Icon Components ---
// Using React.memo to prevent unnecessary re-renders of static icons
const PlayIcon = React.memo(() => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M8 5V19L19 12L8 5Z" fill="currentColor" />
  </svg>
));

const PauseIcon = React.memo(() => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M6 19H10V5H6V19ZM14 5V19H18V5H14Z" fill="currentColor" />
  </svg>
));

const PrevIcon = React.memo(() => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M6 6H8V18H6V6ZM9.5 12L18 18V6L9.5 12Z" fill="currentColor" />
  </svg>
));

const NextIcon = React.memo(() => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 6H18V18H16V6ZM8 18V6L14.5 12L8 18Z" fill="currentColor" />
  </svg>
));

const ResetIcon = React.memo(() => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path
      d="M12 5V1L7 6L12 11V7C15.31 7 18 9.69 18 13C18 16.31 15.31 19 12 19C8.69 19 6 16.31 6 13H4C4 17.42 7.58 21 12 21C16.42 21 20 17.42 20 13C20 8.58 16.42 5 12 5Z"
      fill="currentColor"
    />
  </svg>
));

// --- Main Visualizer Component ---
const LeetCode3622Visualizer = () => {
  // --- State Management ---
  const [n, setN] = useState(99);
  const [inputValue, setInputValue] = useState("99");
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1000); // ms
  const [isDesktop, setIsDesktop] = useState(window.innerWidth > 768);
  const [buttonHover, setButtonHover] = useState({});

  // --- Algorithm Visualization Logic ---
  const visualizationSteps = useMemo(() => {
    const steps = [];
    const original_n = n > 0 ? n : 1; // Ensure n is at least 1 for the logic
    let temp_n = original_n;
    let digit_sum = 0;
    let digit_product = 1;

    // Initial state
    steps.push({
      message: `Start with the number n = ${original_n}. We will calculate the sum and product of its digits.`,
      temp_n,
      digit_sum,
      digit_product,
      original_n,
      digit: null,
      highlight: {n: true},
    });

    if (temp_n > 0) {
      steps.push({
        message: `Start a loop to extract digits while the temporary number (${temp_n}) is greater than 0.`,
        temp_n,
        digit_sum,
        digit_product,
        original_n,
        digit: null,
        highlight: {n: true},
      });
    }

    let processing_n = original_n;

    while (processing_n > 0) {
      const digit = processing_n % 10;

      steps.push({
        message: `Get the last digit: ${processing_n} % 10 = ${digit}.`,
        temp_n: processing_n,
        digit_sum,
        digit_product,
        original_n,
        digit,
        highlight: {n: true, digit: true},
      });

      const new_sum = digit_sum + digit;
      steps.push({
        message: `Add the digit to the sum: ${digit_sum} + ${digit} = ${new_sum}.`,
        temp_n: processing_n,
        digit_sum: new_sum,
        digit_product,
        original_n,
        digit,
        highlight: {digit: true, sum: true},
      });
      digit_sum = new_sum;

      const new_product = digit_product * digit;
      steps.push({
        message: `Multiply the digit into the product: ${digit_product} * ${digit} = ${new_product}.`,
        temp_n: processing_n,
        digit_sum,
        digit_product: new_product,
        original_n,
        digit,
        highlight: {digit: true, product: true},
      });
      digit_product = new_product;

      const next_n = Math.floor(processing_n / 10);
      steps.push({
        message: `Remove the last digit: floor(${processing_n} / 10) = ${next_n}.`,
        temp_n: next_n,
        digit_sum,
        digit_product,
        original_n,
        digit: null,
        highlight: {n: true},
      });
      processing_n = next_n;
    }

    steps.push({
      message: `The loop ends because the temporary number is now 0.`,
      temp_n: 0,
      digit_sum,
      digit_product,
      original_n,
      digit: null,
      highlight: {},
    });

    const total_divisor = digit_sum + digit_product;
    steps.push({
      message: `Calculate the total divisor: sum + product = ${digit_sum} + ${digit_product} = ${total_divisor}.`,
      temp_n: 0,
      digit_sum,
      digit_product,
      original_n,
      total_divisor,
      highlight: {sum: true, product: true, total: true},
    });

    const remainder = original_n % total_divisor;
    const result = remainder === 0;
    steps.push({
      message: `Final check: Is ${original_n} divisible by ${total_divisor}? The remainder of ${original_n} % ${total_divisor} is ${remainder}.`,
      temp_n: 0,
      digit_sum,
      digit_product,
      original_n,
      total_divisor,
      remainder,
      result,
      highlight: {original: true, total: true, final: true},
    });

    steps.push({
      message: `The result is ${result}.`,
      temp_n: 0,
      digit_sum,
      digit_product,
      original_n,
      total_divisor,
      remainder,
      result,
      highlight: {final: true},
    });

    return steps;
  }, [n]);

  const currentVizState = visualizationSteps[currentStep];

  // --- Handlers for Controls ---
  const handleNext = useCallback(() => {
    setCurrentStep((prev) => Math.min(prev + 1, visualizationSteps.length - 1));
  }, [visualizationSteps.length]);

  const handlePrev = () => {
    setCurrentStep((prev) => Math.max(prev - 1, 0));
  };

  const handleReset = () => {
    setCurrentStep(0);
    setIsPlaying(false);
  };

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

  const handleSliderChange = (e) => {
    setCurrentStep(Number(e.target.value));
    setIsPlaying(false);
  };

  const handleInputChange = (e) => {
    const val = e.target.value;
    setInputValue(val);
    const num = parseInt(val, 10);
    if (!isNaN(num) && num >= 1 && num <= 1000000) {
      setN(num);
      setCurrentStep(0);
      setIsPlaying(false);
    }
  };

  // --- Effects ---
  // Playback interval
  useEffect(() => {
    if (isPlaying && currentStep < visualizationSteps.length - 1) {
      const interval = setInterval(() => {
        handleNext();
      }, speed);
      return () => clearInterval(interval);
    }
    if (currentStep === visualizationSteps.length - 1) {
      setIsPlaying(false);
    }
  }, [isPlaying, currentStep, speed, handleNext, visualizationSteps.length]);

  // Responsive layout
  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth > 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // --- Styles ---
  const styles = {
    container: {
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
      backgroundColor: "#f7f7f8",
      display: "flex",
      justifyContent: "center",
      alignItems: "flex-start",
      padding: "1rem",
      minHeight: "100vh",
      boxSizing: "border-box",
    },
    card: {
      backgroundColor: "white",
      borderRadius: "12px",
      boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)",
      borderWidth: "1px",
      borderStyle: "solid",
      borderColor: "#e5e5e5",
      padding: "1rem",
      width: "100%",
      maxWidth: "800px",
      display: "flex",
      flexDirection: isDesktop ? "row" : "column",
      gap: "1rem",
    },
    leftColumn: {
      flex: "1",
      display: "flex",
      flexDirection: "column",
      gap: "1rem",
    },
    rightColumn: {
      flex: "2",
      display: "flex",
      flexDirection: "column",
      gap: "1rem",
    },
    inputGroup: {
      display: "flex",
      flexDirection: "column",
      gap: "0.5rem",
    },
    label: {
      fontWeight: "600",
      fontSize: "0.9rem",
      color: "#333",
    },
    input: {
      padding: "0.5rem 0.75rem",
      borderRadius: "6px",
      borderWidth: "1px",
      borderStyle: "solid",
      borderColor: "#ccc",
      fontSize: "1rem",
      width: "100%",
      boxSizing: "border-box",
    },
    controlsContainer: {
      display: "flex",
      flexDirection: "column",
      gap: "0.75rem",
    },
    buttons: {
      display: "flex",
      justifyContent: "space-between",
      gap: "0.5rem",
    },
    button: {
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      padding: "0.5rem",
      borderWidth: "1px",
      borderStyle: "solid",
      borderColor: "#ccc",
      borderRadius: "6px",
      backgroundColor: "white",
      cursor: "pointer",
      color: "#333",
      transition: "background-color 0.2s, color 0.2s, box-shadow 0.2s",
    },
    buttonHover: {
      backgroundColor: "#007aff",
      color: "white",
      borderColor: "#007aff",
      boxShadow: "0 2px 4px rgba(0, 122, 255, 0.2)",
    },
    slider: {
      width: "100%",
      cursor: "pointer",
    },
    vizArea: {
      borderWidth: "1px",
      borderStyle: "solid",
      borderColor: "#e5e5e5",
      borderRadius: "8px",
      padding: "1rem",
      backgroundColor: "#fafafa",
      minHeight: "200px",
      display: "flex",
      flexDirection: "column",
      gap: "1rem",
      alignItems: "center",
      justifyContent: "center",
    },
    dataRow: {
      display: "flex",
      flexWrap: "wrap",
      gap: "1rem",
      justifyContent: "center",
      alignItems: "center",
    },
    dataBox: {
      padding: "0.5rem 1rem",
      borderRadius: "6px",
      borderWidth: "2px",
      borderStyle: "solid",
      borderColor: "#ccc",
      backgroundColor: "white",
      textAlign: "center",
      transition: "all 0.3s ease-in-out",
    },
    highlighted: {
      borderColor: "#007aff",
      transform: "scale(1.1)",
      boxShadow: "0 2px 8px rgba(0, 122, 255, 0.3)",
    },
    dataLabel: {
      fontSize: "0.75rem",
      color: "#666",
      marginBottom: "0.25rem",
    },
    dataValue: {
      fontSize: "1.25rem",
      fontWeight: "600",
      color: "#333",
    },
    arrow: {
      fontSize: "1.5rem",
      color: "#666",
      fontWeight: "bold",
    },
    actionBox: {
      padding: "0.5rem 0.75rem",
      borderRadius: "6px",
      backgroundColor: "#eef5ff",
      borderWidth: "1px",
      borderStyle: "solid",
      borderColor: "#b3d4ff",
      textAlign: "center",
    },
    actionTitle: {
      fontWeight: "600",
      fontSize: "0.75rem",
      color: "#0052cc",
      margin: "0 0 2px 0",
      padding: "0",
    },
    actionMessage: {
      fontSize: "0.9rem",
      color: "#0052cc",
      margin: "0",
      padding: "0",
    },
    finalResultBox: {
      marginTop: "1rem",
      padding: "1rem",
      borderRadius: "8px",
      textAlign: "center",
      fontWeight: "bold",
      fontSize: "1.2rem",
      transition: "all 0.3s ease-in-out",
    },
    finalTrue: {
      backgroundColor: "#e6f7ec",
      color: "#0f5132",
      borderWidth: "2px",
      borderStyle: "solid",
      borderColor: "#a3cfbb",
    },
    finalFalse: {
      backgroundColor: "#f8d7da",
      color: "#58151c",
      borderWidth: "2px",
      borderStyle: "solid",
      borderColor: "#f1aeb5",
    },
  };

  const getButtonStyle = (name) => ({
    ...styles.button,
    ...(buttonHover[name] ? styles.buttonHover : {}),
  });

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        {/* Left Column: Inputs & Controls */}
        <div style={styles.leftColumn}>
          <div style={styles.inputGroup}>
            <label htmlFor="nInput" style={styles.label}>
              Input Number (n)
            </label>
            <input id="nInput" type="number" value={inputValue} onChange={handleInputChange} style={styles.input} min="1" max="1000000" />
          </div>
          <div style={styles.controlsContainer}>
            <div style={styles.buttons}>
              <button
                style={getButtonStyle("prev")}
                onClick={handlePrev}
                onMouseEnter={() => setButtonHover({prev: true})}
                onMouseLeave={() => setButtonHover({})}
                title="Previous Step"
              >
                <PrevIcon />
              </button>
              <button
                style={getButtonStyle("play")}
                onClick={handlePlayPause}
                onMouseEnter={() => setButtonHover({play: true})}
                onMouseLeave={() => setButtonHover({})}
                title={isPlaying ? "Pause" : "Play"}
              >
                {isPlaying ? <PauseIcon /> : <PlayIcon />}
              </button>
              <button
                style={getButtonStyle("next")}
                onClick={handleNext}
                onMouseEnter={() => setButtonHover({next: true})}
                onMouseLeave={() => setButtonHover({})}
                title="Next Step"
              >
                <NextIcon />
              </button>
              <button
                style={getButtonStyle("reset")}
                onClick={handleReset}
                onMouseEnter={() => setButtonHover({reset: true})}
                onMouseLeave={() => setButtonHover({})}
                title="Reset"
              >
                <ResetIcon />
              </button>
            </div>
            <input type="range" min="0" max={visualizationSteps.length - 1} value={currentStep} onChange={handleSliderChange} style={styles.slider} />
          </div>
        </div>

        {/* Right Column: Visualization */}
        <div style={styles.rightColumn}>
          <div style={styles.vizArea}>
            {/* Top row for calculation */}
            <div style={styles.dataRow}>
              <div style={{...styles.dataBox, ...(currentVizState.highlight?.n && styles.highlighted)}}>
                <div style={styles.dataLabel}>Temp n</div>
                <div style={styles.dataValue}>{currentVizState.temp_n}</div>
              </div>
              {currentVizState.digit !== null && (
                <>
                  <span style={styles.arrow}>→</span>
                  <div style={{...styles.dataBox, ...(currentVizState.highlight?.digit && styles.highlighted)}}>
                    <div style={styles.dataLabel}>Digit</div>
                    <div style={styles.dataValue}>{currentVizState.digit}</div>
                  </div>
                </>
              )}
            </div>

            {/* Bottom row for aggregates */}
            <div style={styles.dataRow}>
              <div style={{...styles.dataBox, ...(currentVizState.highlight?.sum && styles.highlighted)}}>
                <div style={styles.dataLabel}>Digit Sum</div>
                <div style={styles.dataValue}>{currentVizState.digit_sum}</div>
              </div>
              <div style={{...styles.dataBox, ...(currentVizState.highlight?.product && styles.highlighted)}}>
                <div style={styles.dataLabel}>Digit Product</div>
                <div style={styles.dataValue}>{currentVizState.digit_product}</div>
              </div>
            </div>

            {/* Final Calculation */}
            {currentVizState.total_divisor !== undefined && (
              <div style={{...styles.dataRow, marginTop: "1rem"}}>
                <div style={{...styles.dataBox, ...(currentVizState.highlight?.original && styles.highlighted)}}>
                  <div style={styles.dataLabel}>Original n</div>
                  <div style={styles.dataValue}>{currentVizState.original_n}</div>
                </div>
                <span style={styles.arrow}>%</span>
                <div style={{...styles.dataBox, ...(currentVizState.highlight?.total && styles.highlighted)}}>
                  <div style={styles.dataLabel}>Total Divisor</div>
                  <div style={styles.dataValue}>{currentVizState.total_divisor}</div>
                </div>
                <span style={styles.arrow}>=</span>
                <div style={{...styles.dataBox, ...(currentVizState.highlight?.final && styles.highlighted)}}>
                  <div style={styles.dataLabel}>Remainder</div>
                  <div style={styles.dataValue}>{currentVizState.remainder}</div>
                </div>
              </div>
            )}

            {currentVizState.result !== undefined && (
              <div
                style={{
                  ...styles.finalResultBox,
                  ...(currentVizState.result ? styles.finalTrue : styles.finalFalse),
                  ...(currentVizState.highlight?.final && {transform: "scale(1.05)"}),
                }}
              >
                Result: {String(currentVizState.result)}
              </div>
            )}
          </div>
          <div style={styles.actionBox}>
            <p style={styles.actionTitle}>CURRENT ACTION</p>
            <p style={styles.actionMessage}>{currentVizState.message}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LeetCode3622Visualizer;
