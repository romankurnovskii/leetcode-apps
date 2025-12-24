import React, { useState, useMemo, useEffect, useRef } from "react";

// SVG Icon Components
const PlayIcon = (props) => (
  <svg width={20} height={20} viewBox="0 0 20 20" fill="none" {...props}>
    <path d="M6 4L16 10L6 16V4Z" fill="#007aff" />
  </svg>
);
const PauseIcon = (props) => (
  <svg width={20} height={20} viewBox="0 0 20 20" fill="none" {...props}>
    <rect x="5" y="4" width="3" height="12" rx="1" fill="#007aff" />
    <rect x="12" y="4" width="3" height="12" rx="1" fill="#007aff" />
  </svg>
);
const NextIcon = (props) => (
  <svg width={20} height={20} viewBox="0 0 20 20" fill="none" {...props}>
    <path d="M7 5L13 10L7 15V5Z" fill="#007aff" />
  </svg>
);
const PrevIcon = (props) => (
  <svg width={20} height={20} viewBox="0 0 20 20" fill="none" {...props}>
    <path d="M13 5L7 10L13 15V5Z" fill="#007aff" />
  </svg>
);
const ResetIcon = (props) => (
  <svg width={20} height={20} viewBox="0 0 20 20" fill="none" {...props}>
    <path
      d="M10 4V2M10 2C5.58 2 2 5.58 2 10C2 14.42 5.58 18 10 18C14.42 18 18 14.42 18 10C18 8.13 17.37 6.41 16.32 5.05M10 2V6M10 2L13 5"
      stroke="#007aff"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

function isVowel(c) {
  return "aeiouAEIOU".includes(c);
}

function generateVisualization(inputString) {
  // Based on the greedy solution in 01.py and the explanation
  const s = inputString;
  if (!s) return [];
  const steps = [];
  let res = s[0];
  let count = 1;
  steps.push({
    i: 0,
    res: res,
    count: 1,
    char: s[0],
    action: "init",
    message: `Start with the first character: '${s[0]}' (count = 1). Add to result.`,
    highlight: [0],
    skip: false,
  });
  for (let i = 1; i < s.length; i++) {
    const prevChar = res[res.length - 1];
    let message = "";
    let skip = false;
    if (s[i] === prevChar) {
      count += 1;
      if (count < 3) {
        res += s[i];
        message = `Character '${s[i]}' is the same as previous. Count = ${count} (< 3), so add to result.`;
      } else {
        message = `Character '${s[i]}' is the same as previous. Count = ${count} (>= 3), so skip (delete) this character.`;
        skip = true;
      }
    } else {
      count = 1;
      res += s[i];
      message = `Character '${s[i]}' is different from previous. Reset count to 1 and add to result.`;
    }
    steps.push({
      i,
      res,
      count,
      char: s[i],
      action: skip ? "skip" : "add",
      message,
      highlight: [i],
      skip,
    });
  }
  steps.push({
    i: s.length,
    res,
    count: null,
    char: null,
    action: "done",
    message: `Done. Final fancy string: "${res}"`,
    highlight: [],
    skip: false,
  });
  return steps;
}

const defaultInput = "aaabaaaa";

const FancyStringVisualizer = () => {
  // State
  const [input, setInput] = useState(defaultInput);
  const [visualizationSteps, setVisualizationSteps] = useState(() => generateVisualization(defaultInput));
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(900);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const playRef = useRef();

  // Responsive layout
  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth >= 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // Regenerate steps when input changes
  useEffect(() => {
    const steps = generateVisualization(input);
    setVisualizationSteps(steps);
    setCurrentStep(0);
    setIsPlaying(false);
  }, [input]);

  // Playback effect
  useEffect(() => {
    if (isPlaying) {
      if (currentStep < visualizationSteps.length - 1) {
        playRef.current = setTimeout(() => setCurrentStep((s) => s + 1), speed);
      } else {
        setIsPlaying(false);
      }
    }
    return () => clearTimeout(playRef.current);
  }, [isPlaying, currentStep, visualizationSteps.length, speed]);

  // Controls
  const goToStep = (idx) => {
    setCurrentStep(idx);
    setIsPlaying(false);
  };
  const handlePrev = () => goToStep(Math.max(0, currentStep - 1));
  const handleNext = () => goToStep(Math.min(visualizationSteps.length - 1, currentStep + 1));
  const handleReset = () => goToStep(0);
  const handlePlayPause = () => setIsPlaying((p) => !p);

  // Step data
  const step = visualizationSteps[currentStep] || {};
  const chars = input.split("");
  const resChars = (step.res || "").split("");

  // Styles
  const card = {
    background: "#fff",
    borderRadius: 12,
    boxShadow: "0 2px 12px rgba(0,0,0,0.07)",
    maxWidth: 820,
    margin: "2rem auto",
    display: "flex",
    flexDirection: isDesktop ? "row" : "column",
    padding: isDesktop ? "1.5rem 2rem" : "1rem 0.5rem",
    gap: isDesktop ? 32 : 16,
    border: "1px solid #e5e5e5",
  };
  const leftCol = { flex: 1, minWidth: 220, marginBottom: isDesktop ? 0 : 16 };
  const rightCol = { flex: 2, minWidth: 0 };
  const label = { fontSize: 14, fontWeight: 500, marginBottom: 4 };
  const inputBox = {
    width: "100%",
    fontSize: 16,
    padding: "0.5rem",
    border: "1px solid #e5e5e5",
    borderRadius: 6,
    marginBottom: 12,
    background: "#f7f7f8",
  };
  const controls = {
    display: "flex",
    alignItems: "center",
    gap: 8,
    margin: "12px 0 4px 0",
  };
  const slider = { width: "100%", margin: "8px 0" };
  const stepDisplay = { fontSize: 13, color: "#555", margin: "0 0 4px 0" };
  const vizArea = {
    background: "#f7f7f8",
    borderRadius: 8,
    padding: isDesktop ? "1.25rem 1.5rem" : "0.75rem 0.5rem",
    border: "1px solid #e5e5e5",
    minHeight: 120,
    marginBottom: 10,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
  };
  const strRow = { display: "flex", gap: 6, flexWrap: "wrap", marginBottom: 8 };
  const charBox = (active, skipped) => ({
    minWidth: 32,
    minHeight: 38,
    fontSize: 22,
    fontWeight: 600,
    borderRadius: 6,
    border: `2px solid ${active ? "#007aff" : "#e5e5e5"}`,
    background: skipped ? "#ffeaea" : active ? "#eaf4ff" : "#fff",
    color: skipped ? "#c00" : "#222",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    transition: "all 0.2s",
    boxShadow: active ? "0 1px 4px #007aff22" : "none",
  });
  const resRow = { display: "flex", gap: 6, flexWrap: "wrap", marginTop: 8 };
  const msgBox = {
    background: "#f7f7f8",
    border: "1px solid #e5e5e5",
    borderRadius: 6,
    fontSize: 13,
    padding: "0.25rem 0.5rem",
    marginTop: 8,
    color: "#333",
    minHeight: 32,
  };
  const msgTitle = { fontSize: 12, fontWeight: 600, color: "#888", marginBottom: 2 };

  return (
    <div style={card}>
      {/* Left Column: Inputs & Controls */}
      <div style={leftCol}>
        <div style={label}>Input String</div>
        <input
          style={inputBox}
          value={input}
          onChange={(e) => setInput(e.target.value.replace(/[^a-z]/g, ""))}
          maxLength={100}
          spellCheck={false}
          autoComplete="off"
          aria-label="Input string"
        />
        <div style={controls}>
          <button onClick={handlePrev} disabled={currentStep === 0} style={{ background: "none", border: "none", padding: 2, cursor: "pointer" }}>
            <PrevIcon />
          </button>
          <button onClick={handlePlayPause} style={{ background: "none", border: "none", padding: 2, cursor: "pointer" }}>
            {isPlaying ? <PauseIcon /> : <PlayIcon />}
          </button>
          <button
            onClick={handleNext}
            disabled={currentStep === visualizationSteps.length - 1}
            style={{ background: "none", border: "none", padding: 2, cursor: "pointer" }}
          >
            <NextIcon />
          </button>
          <button onClick={handleReset} style={{ background: "none", border: "none", padding: 2, cursor: "pointer" }}>
            <ResetIcon />
          </button>
        </div>
        <div style={stepDisplay}>
          Step {currentStep + 1} of {visualizationSteps.length}
        </div>
        <input
          type="range"
          min={0}
          max={visualizationSteps.length - 1}
          value={currentStep}
          onChange={(e) => goToStep(Number(e.target.value))}
          style={slider}
          aria-label="Step slider"
        />
      </div>
      {/* Right Column: Visualization */}
      <div style={rightCol}>
        <div style={vizArea}>
          <div style={{ ...strRow, marginBottom: 2 }}>
            {chars.map((c, idx) => (
              <div
                key={idx}
                style={charBox(step.highlight && step.highlight.includes(idx), step.skip && step.i === idx)}
                aria-label={`Input char ${c} at position ${idx}`}
              >
                {c}
              </div>
            ))}
          </div>
          <div style={{ fontSize: 13, color: "#888", marginBottom: 2 }}>Result so far:</div>
          <div style={resRow}>
            {resChars.map((c, idx) => (
              <div key={idx} style={charBox(false, false)} aria-label={`Result char ${c} at position ${idx}`}>
                {c}
              </div>
            ))}
          </div>
        </div>
        <div style={msgBox}>
          <div style={msgTitle}>Current Action</div>
          <div>{step.message}</div>
        </div>
      </div>
    </div>
  );
};

export default FancyStringVisualizer;
