import React, {useState, useEffect, useMemo} from "react";

// --- SVG Icon Components ---
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

// --- Main Visualizer Component ---
export default function MaximumNumberOfConsecutiveValuesYouCanMakeVisualizer() {
  // --- State Management ---
  const [coins, setCoins] = useState([1, 1, 1, 4]);
  const [inputString, setInputString] = useState("1,1,1,4");
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1000);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hover, setHover] = useState({prev: false, play: false, next: false, reset: false});

  // --- Visualization Logic ---
  const generateVisualization = useMemo(() => {
    return (coinsArr) => {
      const steps = [];
      const sorted = [...coinsArr].sort((a, b) => a - b);
      let res = 1;
      let i = 0;
      // Initial state
      steps.push({
        type: "initial",
        sorted: [...sorted],
        res,
        i: null,
        message: "Start with the sorted coins array. res = 1 (smallest value we cannot make yet).",
      });
      // Step through each coin
      for (i = 0; i < sorted.length; i++) {
        const coin = sorted[i];
        steps.push({
          type: "check_coin",
          sorted: [...sorted],
          res,
          i,
          coin,
          message: `Checking coin at index ${i}: value = ${coin}. Current res = ${res}.`,
        });
        if (coin > res) {
          steps.push({
            type: "gap_found",
            sorted: [...sorted],
            res,
            i,
            coin,
            message: `Coin value ${coin} > res (${res}). Cannot make value ${res}. Stop.`,
          });
          break;
        } else {
          steps.push({
            type: "add_coin",
            sorted: [...sorted],
            res,
            i,
            coin,
            newRes: res + coin,
            message: `Coin value ${coin} <= res (${res}). We can now make all values up to ${res + coin - 1}. Update res = ${res + coin}.`,
          });
          res += coin;
        }
      }
      // Final state
      steps.push({
        type: "final",
        sorted: [...sorted],
        res,
        i: i < sorted.length ? i : null,
        message: `Done. The maximum number of consecutive values you can make is ${res}.`,
      });
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
    const {steps} = generateVisualization(coins);
    setVisualizationSteps(steps);
    setCurrentStep(0);
    setIsPlaying(false);
  }, [coins, generateVisualization]);

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
  const handleInputChange = (e) => {
    setInputString(e.target.value);
    const arr = e.target.value
      .split(",")
      .map((x) => parseInt(x.trim(), 10))
      .filter((x) => !isNaN(x));
    setCoins(arr);
  };

  // --- Styles ---
  const palette = {
    background: "#f7f7f8",
    card: "#fff",
    border: "#e5e5e5",
    primary: "#007aff",
    text: "#222",
    highlight: "#eaf6ff",
    active: "#007aff22",
  };
  const cardStyle = {
    background: palette.card,
    border: `1px solid ${palette.border}`,
    borderRadius: 12,
    maxWidth: 820,
    margin: "2rem auto",
    boxShadow: "0 2px 8px 0 #0001",
    display: "flex",
    flexDirection: isDesktop ? "row" : "column",
    padding: isDesktop ? "1.5rem 2rem" : "1rem 0.5rem",
  };
  const leftCol = {flex: 1, minWidth: 220, marginRight: isDesktop ? 32 : 0, marginBottom: isDesktop ? 0 : 24};
  const rightCol = {flex: 2, minWidth: 0, display: "flex", flexDirection: "column", alignItems: "center"};
  const inputStyle = {
    width: "100%",
    padding: "0.5rem",
    border: `1px solid ${palette.border}`,
    borderRadius: 6,
    fontSize: 16,
    marginBottom: 12,
  };
  const controlsRow = {display: "flex", alignItems: "center", gap: 8, margin: "0.5rem 0"};
  const sliderStyle = {width: "100%", margin: "0.5rem 0"};
  const vizArea = {
    background: palette.background,
    border: `1px solid ${palette.border}`,
    borderRadius: 8,
    padding: "1rem",
    minHeight: 90,
    width: "100%",
    marginBottom: 12,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  };
  const coinsRow = {display: "flex", gap: 8, margin: "0.5rem 0"};
  const coinStyle = (active, processed) => ({
    padding: "0.5rem 0.9rem",
    borderRadius: 6,
    border: `2px solid ${active ? palette.primary : palette.border}`,
    background: active ? palette.highlight : processed ? palette.active : "#fff",
    color: palette.text,
    fontWeight: active ? 700 : 500,
    fontSize: 18,
    transform: active ? "scale(1.12)" : "none",
    transition: "all 0.2s",
  });
  const resBox = {
    margin: "0.5rem 0",
    padding: "0.25rem 0.5rem",
    border: `1px solid ${palette.primary}`,
    borderRadius: 6,
    background: "#f7fbff",
    fontSize: 16,
    fontWeight: 600,
    color: palette.primary,
    display: "inline-block",
  };
  const actionBox = {
    background: "#f7f7f8",
    border: `1px solid ${palette.border}`,
    borderRadius: 6,
    padding: "0.25rem 0.5rem",
    fontSize: 13,
    marginTop: 2,
    marginBottom: 0,
    color: palette.text,
    minHeight: 28,
  };

  // --- Visualization Frame Renderer ---
  const renderFrame = () => {
    const step = visualizationSteps[currentStep] || {};
    const {sorted = [], res, i, coin, newRes, type} = step;
    // Mark processed coins
    const processed = i == null ? [] : Array(i).fill(true);
    return (
      <div style={vizArea}>
        <div style={{fontSize: 15, marginBottom: 6}}>Sorted Coins:</div>
        <div style={coinsRow}>
          {sorted.map((val, idx) => (
            <div key={idx} style={coinStyle(idx === i, processed[idx])}>
              {val}
            </div>
          ))}
        </div>
        <div style={{margin: "0.5rem 0 0.25rem 0"}}>
          <span style={resBox}>res = {res}</span>
          {type === "add_coin" && newRes !== undefined && (
            <span style={{marginLeft: 12, color: palette.primary, fontWeight: 500}}>
              → res + coin = {res - coin} + {coin} = {newRes}
            </span>
          )}
        </div>
      </div>
    );
  };

  // --- Main Render ---
  return (
    <div style={{background: palette.background, minHeight: "100vh", padding: 0}}>
      <div style={cardStyle}>
        {/* Left Column: Inputs & Controls */}
        <div style={leftCol}>
          <div style={{fontWeight: 600, fontSize: 18, marginBottom: 8}}>Maximum Number of Consecutive Values You Can Make</div>
          <div style={{fontSize: 14, marginBottom: 4}}>Coins (comma-separated):</div>
          <input type="text" value={inputString} onChange={handleInputChange} style={inputStyle} spellCheck={false} autoComplete="off" />
          <div style={controlsRow}>
            <button
              style={{
                background: "none",
                border: "none",
                cursor: "pointer",
                padding: 4,
                borderRadius: 4,
                outline: hover.prev ? `1.5px solid ${palette.primary}` : "none",
              }}
              onClick={handlePrevious}
              onMouseEnter={() => handleHover("prev", true)}
              onMouseLeave={() => handleHover("prev", false)}
              disabled={currentStep === 0}
              aria-label="Previous"
            >
              <PrevIcon />
            </button>
            <button
              style={{
                background: "none",
                border: "none",
                cursor: "pointer",
                padding: 4,
                borderRadius: 4,
                outline: hover.play ? `1.5px solid ${palette.primary}` : "none",
              }}
              onClick={handlePlayPause}
              onMouseEnter={() => handleHover("play", true)}
              onMouseLeave={() => handleHover("play", false)}
              aria-label={isPlaying ? "Pause" : "Play"}
            >
              {isPlaying ? <PauseIcon /> : <PlayIcon />}
            </button>
            <button
              style={{
                background: "none",
                border: "none",
                cursor: "pointer",
                padding: 4,
                borderRadius: 4,
                outline: hover.next ? `1.5px solid ${palette.primary}` : "none",
              }}
              onClick={handleNext}
              onMouseEnter={() => handleHover("next", true)}
              onMouseLeave={() => handleHover("next", false)}
              disabled={currentStep === visualizationSteps.length - 1}
              aria-label="Next"
            >
              <NextIcon />
            </button>
            <button
              style={{
                background: "none",
                border: "none",
                cursor: "pointer",
                padding: 4,
                borderRadius: 4,
                outline: hover.reset ? `1.5px solid ${palette.primary}` : "none",
              }}
              onClick={handleReset}
              onMouseEnter={() => handleHover("reset", true)}
              onMouseLeave={() => handleHover("reset", false)}
              aria-label="Reset"
            >
              <ResetIcon />
            </button>
          </div>
          <input type="range" min={0} max={visualizationSteps.length - 1} value={currentStep} onChange={handleSliderChange} style={sliderStyle} />
          <div style={{fontSize: 12, color: "#888", textAlign: "center"}}>
            Step {currentStep + 1} / {visualizationSteps.length}
          </div>
        </div>
        {/* Right Column: Visualization & Action Message */}
        <div style={rightCol}>
          {renderFrame()}
          <div style={actionBox}>
            <div style={{fontWeight: 600, fontSize: 12, marginBottom: 2}}>Current Action</div>
            <div style={{fontSize: 13, margin: 0}}>{visualizationSteps[currentStep]?.message}</div>
          </div>
        </div>
      </div>
    </div>
  );
}
