import React, {useState, useMemo, useEffect} from "react";

// SVG Icon Components
const PrevIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M13 15l-5-5 5-5" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);
const NextIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M7 5l5 5-5 5" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);
const PlayIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M7 5v10l8-5-8-5z" fill={color} />
  </svg>
);
const PauseIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <rect x="6" y="5" width="2.5" height="10" rx="1" fill={color} />
    <rect x="11.5" y="5" width="2.5" height="10" rx="1" fill={color} />
  </svg>
);
const ResetIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M4 10a6 6 0 1 1 2 4.47" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M4 14v-4h4" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

function clamp(val, min, max) {
  return Math.max(min, Math.min(max, val));
}

const defaultWord1 = "abc";
const defaultWord2 = "pqr";

const containerStyle = {
  background: "#f7f7f8",
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  minHeight: undefined, // Remove minHeight
  padding: "1.5rem 0", // Reduce vertical padding
};
const cardStyle = (isDesktop) => ({
  background: "#fff",
  border: "1px solid #e5e5e5",
  borderRadius: "1rem",
  boxShadow: "0 2px 8px rgba(0,0,0,0.03)",
  display: "flex",
  flexDirection: isDesktop ? "row" : "column",
  width: "100%",
  maxWidth: isDesktop ? 820 : "98vw", // Use as much width as possible, up to 820px
  margin: "0 auto",
  alignItems: "stretch",
  overflow: "hidden",
});
const leftColStyle = (isDesktop) => ({
  flex: 1,
  minWidth: 0,
  borderRight: isDesktop ? "1px solid #e5e5e5" : "none",
  padding: isDesktop ? "1rem" : "0.75rem",
  display: "flex",
  flexDirection: "column",
  gap: "1rem",
  background: "#fafbfc",
});
const rightColStyle = (isDesktop) => ({
  flex: 2,
  minWidth: 0,
  padding: isDesktop ? "1rem" : "0.75rem",
  display: "flex",
  flexDirection: "column",
  gap: "0.75rem",
  justifyContent: "flex-start",
});
const inputStyle = {
  width: "100%",
  fontSize: "1rem",
  padding: "0.25rem 0.5rem",
  border: "1px solid #e5e5e5",
  borderRadius: "0.5rem",
  background: "#fff",
  marginBottom: "0.25rem",
};
const labelStyle = {
  fontSize: "0.85rem",
  fontWeight: 500,
  marginBottom: "0.15rem",
  color: "#222",
};
const controlsRowStyle = {
  display: "flex",
  alignItems: "center",
  gap: "0.5rem",
  margin: "0.25rem 0",
};
const sliderStyle = {
  width: "100%",
  margin: "0.5rem 0",
};
const actionBoxStyle = {
  background: "#f7f7f8",
  border: "1px solid #e5e5e5",
  borderRadius: "0.5rem",
  padding: "0.25rem 0.5rem",
  fontSize: "0.75rem",
  margin: 0,
  minHeight: "2.2em",
  display: "flex",
  alignItems: "center",
};
const visAreaStyle = {
  background: "#fff",
  border: "1px solid #e5e5e5",
  borderRadius: "0.5rem",
  padding: "0.75rem",
  minHeight: "70px",
  display: "flex",
  flexDirection: "column",
  gap: "0.5rem",
  alignItems: "center",
  justifyContent: "center",
};
const arrayRowStyle = {
  display: "flex",
  gap: "0.25rem",
  flexWrap: "wrap",
  alignItems: "center",
};
const charBoxStyle = (active, faded) => ({
  border: "1px solid",
  borderColor: active ? "#007aff" : "#e5e5e5",
  background: active ? "#eaf4ff" : faded ? "#f7f7f8" : "#fff",
  color: "#222",
  borderRadius: "0.4rem",
  padding: "0.25rem 0.5rem",
  fontWeight: 600,
  fontSize: "1.1rem",
  minWidth: "1.5rem",
  textAlign: "center",
  transform: active ? "scale(1.12)" : "none",
  transition: "all 0.2s",
  opacity: faded ? 0.5 : 1,
});
const mergedBoxStyle = {
  border: "1px solid #e5e5e5",
  background: "#fafbfc",
  borderRadius: "0.4rem",
  padding: "0.25rem 0.5rem",
  fontWeight: 600,
  fontSize: "1.1rem",
  minWidth: "1.5rem",
  textAlign: "center",
  margin: "0 0.1rem",
};

function generateVisualization(word1, word2) {
  const steps = [];
  const n1 = word1.length,
    n2 = word2.length;
  let i = 0;
  let merged = [];
  // Initial step
  steps.push({
    type: "initial",
    i,
    merged: [...merged],
    word1,
    word2,
    message: "Start with both strings and an empty merged result.",
  });
  // Alternating merge
  while (i < n1 && i < n2) {
    steps.push({
      type: "pick_word1",
      i,
      merged: [...merged],
      word1,
      word2,
      message: `Add word1[${i}] ('${word1[i]}') to merged.`,
    });
    merged.push(word1[i]);
    steps.push({
      type: "pick_word2",
      i,
      merged: [...merged],
      word1,
      word2,
      message: `Add word2[${i}] ('${word2[i]}') to merged.`,
    });
    merged.push(word2[i]);
    i++;
  }
  // Append leftovers
  if (i < n1) {
    steps.push({
      type: "append_word1",
      i,
      merged: [...merged],
      word1,
      word2,
      message: `word2 is done. Append the rest of word1 ('${word1.slice(i)}') to merged.`,
    });
    merged = merged.concat(word1.slice(i).split(""));
  } else if (i < n2) {
    steps.push({
      type: "append_word2",
      i,
      merged: [...merged],
      word1,
      word2,
      message: `word1 is done. Append the rest of word2 ('${word2.slice(i)}') to merged.`,
    });
    merged = merged.concat(word2.slice(i).split(""));
  }
  // Final step
  steps.push({
    type: "final",
    i,
    merged: [...merged],
    word1,
    word2,
    message: `Done! The merged string is '${merged.join("")}'.`,
  });
  return steps;
}

const MergeStringsAlternatelyVisualizer = () => {
  const [word1, setWord1] = useState(defaultWord1);
  const [word2, setWord2] = useState(defaultWord2);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1.2); // seconds per step
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hoverBtn, setHoverBtn] = useState("");
  const steps = useMemo(() => generateVisualization(word1, word2), [word1, word2]);
  const maxStep = steps.length - 1;

  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth >= 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    setCurrentStep(0);
    setIsPlaying(false);
  }, [word1, word2]);

  useEffect(() => {
    if (!isPlaying) return;
    if (currentStep >= maxStep) {
      setIsPlaying(false);
      return;
    }
    const interval = setInterval(() => {
      setCurrentStep((s) => {
        if (s < maxStep) return s + 1;
        setIsPlaying(false);
        return s;
      });
    }, speed * 1000);
    return () => clearInterval(interval);
  }, [isPlaying, currentStep, speed, maxStep]);

  const step = steps[currentStep];

  // Handlers
  const handlePrev = () => setCurrentStep((s) => clamp(s - 1, 0, maxStep));
  const handleNext = () => setCurrentStep((s) => clamp(s + 1, 0, maxStep));
  const handleReset = () => {
    setCurrentStep(0);
    setIsPlaying(false);
  };
  const handlePlayPause = () => {
    if (currentStep === maxStep) setCurrentStep(0);
    setIsPlaying((p) => !p);
  };
  const handleSlider = (e) => {
    setIsPlaying(false);
    setCurrentStep(Number(e.target.value));
  };
  const handleSpeed = (e) => setSpeed(Number(e.target.value));

  // Input validation
  const handleWord1 = (e) => {
    const val = e.target.value.replace(/[^a-z]/g, "");
    setWord1(val.slice(0, 100));
  };
  const handleWord2 = (e) => {
    const val = e.target.value.replace(/[^a-z]/g, "");
    setWord2(val.slice(0, 100));
  };

  // Visualization rendering
  const renderArray = (arr, activeIdx, fadedFrom) => (
    <div style={arrayRowStyle}>
      {arr.split("").map((ch, idx) => (
        <div key={idx} style={charBoxStyle(idx === activeIdx, fadedFrom !== undefined && idx >= fadedFrom)}>
          {ch}
        </div>
      ))}
    </div>
  );
  const renderMerged = (mergedArr) => (
    <div style={arrayRowStyle}>
      {mergedArr.map((ch, idx) => (
        <div key={idx} style={mergedBoxStyle}>
          {ch}
        </div>
      ))}
    </div>
  );

  // Determine which char is active
  let activeWord1 = null,
    activeWord2 = null,
    fadedWord1 = null,
    fadedWord2 = null;
  if (step.type === "pick_word1") activeWord1 = step.i;
  if (step.type === "pick_word2") activeWord2 = step.i;
  if (step.type === "append_word1") fadedWord1 = step.i;
  if (step.type === "append_word2") fadedWord2 = step.i;

  return (
    <div style={containerStyle}>
      <div style={cardStyle(isDesktop)}>
        {/* Left Column: Inputs and Controls */}
        <div style={leftColStyle(isDesktop)}>
          <div>
            <div style={labelStyle}>word1</div>
            <input style={inputStyle} value={word1} onChange={handleWord1} maxLength={100} autoComplete="off" spellCheck={false} />
          </div>
          <div>
            <div style={labelStyle}>word2</div>
            <input style={inputStyle} value={word2} onChange={handleWord2} maxLength={100} autoComplete="off" spellCheck={false} />
          </div>
          <div>
            <div style={labelStyle}>Speed: {speed.toFixed(2)}s/step</div>
            <input style={{width: "100%"}} type="range" min={0.3} max={2.5} step={0.01} value={speed} onChange={handleSpeed} />
          </div>
          <div style={controlsRowStyle}>
            <button
              style={{
                background: "none",
                border: "none",
                padding: 2,
                cursor: currentStep === 0 ? "not-allowed" : "pointer",
                opacity: currentStep === 0 ? 0.5 : 1,
                borderRadius: 6,
                outline: "none",
              }}
              onClick={handlePrev}
              disabled={currentStep === 0}
              onMouseEnter={() => setHoverBtn("prev")}
              onMouseLeave={() => setHoverBtn("")}
              aria-label="Previous"
            >
              <PrevIcon color={hoverBtn === "prev" ? "#0051a8" : "#007aff"} />
            </button>
            <button
              style={{background: "none", border: "none", padding: 2, cursor: "pointer", borderRadius: 6, outline: "none"}}
              onClick={handlePlayPause}
              onMouseEnter={() => setHoverBtn("play")}
              onMouseLeave={() => setHoverBtn("")}
              aria-label={isPlaying ? "Pause" : "Play"}
            >
              {isPlaying ? (
                <PauseIcon color={hoverBtn === "play" ? "#0051a8" : "#007aff"} />
              ) : (
                <PlayIcon color={hoverBtn === "play" ? "#0051a8" : "#007aff"} />
              )}
            </button>
            <button
              style={{
                background: "none",
                border: "none",
                padding: 2,
                cursor: currentStep === maxStep ? "not-allowed" : "pointer",
                opacity: currentStep === maxStep ? 0.5 : 1,
                borderRadius: 6,
                outline: "none",
              }}
              onClick={handleNext}
              disabled={currentStep === maxStep}
              onMouseEnter={() => setHoverBtn("next")}
              onMouseLeave={() => setHoverBtn("")}
              aria-label="Next"
            >
              <NextIcon color={hoverBtn === "next" ? "#0051a8" : "#007aff"} />
            </button>
            <button
              style={{background: "none", border: "none", padding: 2, cursor: "pointer", borderRadius: 6, outline: "none"}}
              onClick={handleReset}
              onMouseEnter={() => setHoverBtn("reset")}
              onMouseLeave={() => setHoverBtn("")}
              aria-label="Reset"
            >
              <ResetIcon color={hoverBtn === "reset" ? "#0051a8" : "#007aff"} />
            </button>
          </div>
          <input style={sliderStyle} type="range" min={0} max={maxStep} value={currentStep} onChange={handleSlider} />
          <div style={{fontSize: "0.75rem", color: "#888", textAlign: "center"}}>
            Step {currentStep + 1} / {steps.length}
          </div>
        </div>
        {/* Right Column: Visualization and Action */}
        <div style={rightColStyle(isDesktop)}>
          <div style={visAreaStyle}>
            <div style={{fontSize: "0.85rem", fontWeight: 500, marginBottom: 2}}>word1</div>
            {renderArray(step.word1, activeWord1, fadedWord1)}
            <div style={{fontSize: "0.85rem", fontWeight: 500, margin: "0.25rem 0 2px 0"}}>word2</div>
            {renderArray(step.word2, activeWord2, fadedWord2)}
            <div style={{fontSize: "0.85rem", fontWeight: 500, margin: "0.25rem 0 2px 0"}}>merged</div>
            {renderMerged(step.merged)}
          </div>
          <div style={actionBoxStyle}>
            <span style={{fontWeight: 600, marginRight: 6}}>Current Action:</span> {step.message}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MergeStringsAlternatelyVisualizer;
