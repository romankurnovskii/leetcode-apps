import React, { useState, useMemo, useEffect } from "react";

// SVG Icon Components
const PrevIcon = ({ color = "#007aff" }) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M13 15l-5-5 5-5" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);
const NextIcon = ({ color = "#007aff" }) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M7 5l5 5-5 5" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);
const PlayIcon = ({ color = "#007aff" }) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M7 5v10l8-5-8-5z" fill={color} />
  </svg>
);
const PauseIcon = ({ color = "#007aff" }) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <rect x="6" y="5" width="2.5" height="10" rx="1" fill={color} />
    <rect x="11.5" y="5" width="2.5" height="10" rx="1" fill={color} />
  </svg>
);
const ResetIcon = ({ color = "#007aff" }) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M4 10a6 6 0 1 1 2 4.47" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M4 14v-4h4" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

function clamp(val, min, max) {
  return Math.max(min, Math.min(max, val));
}

const defaultNums1 = "1,2,3";
const defaultNums2 = "2,4,6";

const containerStyle = {
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  width: "100%",
  minHeight: 0,
  background: "#fff",
  padding: 0,
};
const cardStyle = (isDesktop) => ({
  background: "#fff",
  border: "1px solid #e5e5e5",
  borderRadius: "1rem",
  boxShadow: "0 2px 8px rgba(0,0,0,0.03)",
  display: "flex",
  flexDirection: isDesktop ? "row" : "column",
  width: isDesktop ? 600 : "95vw",
  maxWidth: "98vw",
  marginTop: 0,
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
  minHeight: "90px",
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
const numBoxStyle = (active, faded, color) => ({
  border: "1.5px solid",
  borderColor: color || (active ? "#007aff" : "#e5e5e5"),
  background: active ? "#eaf4ff" : faded ? "#f7f7f8" : "#fff",
  color: "#222",
  borderRadius: "0.4rem",
  padding: "0.25rem 0.6rem",
  fontWeight: 600,
  fontSize: "1.1rem",
  minWidth: "2.1rem",
  textAlign: "center",
  transform: active ? "scale(1.12)" : "none",
  transition: "all 0.2s",
  opacity: faded ? 0.5 : 1,
});
const resultBoxStyle = {
  border: "1.5px solid #00b894",
  background: "#eafbe7",
  borderRadius: "0.4rem",
  padding: "0.25rem 0.6rem",
  fontWeight: 600,
  fontSize: "1.1rem",
  minWidth: "2.1rem",
  textAlign: "center",
  margin: "0 0.1rem",
};

function parseNums(str) {
  return str
    .split(",")
    .map((s) => parseInt(s.trim(), 10))
    .filter((x) => !isNaN(x));
}

function generateVisualization(nums1Str, nums2Str) {
  const nums1 = parseNums(nums1Str);
  const nums2 = parseNums(nums2Str);
  const steps = [];
  // Initial step
  steps.push({
    type: "initial",
    nums1: [...nums1],
    nums2: [...nums2],
    set1: new Set(),
    set2: new Set(),
    diff1: [],
    diff2: [],
    message: "Imagine you have two boxes of colored marbles (numbers). Let's see which colors are unique to each box!",
  });
  // Build sets
  steps.push({
    type: "build_sets",
    nums1: [...nums1],
    nums2: [...nums2],
    set1: new Set(nums1),
    set2: new Set(nums2),
    diff1: [],
    diff2: [],
    message:
      "We use sets to quickly find all unique marbles in each box. Sets help us check for differences much faster than searching through the whole box.",
  });
  // Find nums1 - nums2
  let diff1 = [];
  for (let i = 0; i < nums1.length; ++i) {
    const n = nums1[i];
    if (!nums2.includes(n) && !diff1.includes(n)) {
      diff1.push(n);
      steps.push({
        type: "diff1",
        nums1: [...nums1],
        nums2: [...nums2],
        set1: new Set(nums1),
        set2: new Set(nums2),
        diff1: [...diff1],
        diff2: [],
        current: n,
        message: `Marble color ${n} is in the first box but not in the second. Add it to the first result list!`,
      });
    }
  }
  // Find nums2 - nums1
  let diff2 = [];
  for (let i = 0; i < nums2.length; ++i) {
    const n = nums2[i];
    if (!nums1.includes(n) && !diff2.includes(n)) {
      diff2.push(n);
      steps.push({
        type: "diff2",
        nums1: [...nums1],
        nums2: [...nums2],
        set1: new Set(nums1),
        set2: new Set(nums2),
        diff1: [...diff1],
        diff2: [...diff2],
        current: n,
        message: `Marble color ${n} is in the second box but not in the first. Add it to the second result list!`,
      });
    }
  }
  // Final step
  steps.push({
    type: "final",
    nums1: [...nums1],
    nums2: [...nums2],
    set1: new Set(nums1),
    set2: new Set(nums2),
    diff1: [...diff1],
    diff2: [...diff2],
    message: `All done! The first list shows marbles only in the first box, and the second list shows marbles only in the second box.`,
  });
  return steps;
}

const FindDifferenceOfTwoArraysVisualizer = () => {
  const [nums1Str, setNums1Str] = useState(defaultNums1);
  const [nums2Str, setNums2Str] = useState(defaultNums2);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1.2); // seconds per step
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hoverBtn, setHoverBtn] = useState("");
  const steps = useMemo(() => generateVisualization(nums1Str, nums2Str), [nums1Str, nums2Str]);
  const maxStep = steps.length - 1;

  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth >= 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    setCurrentStep(0);
    setIsPlaying(false);
  }, [nums1Str, nums2Str]);

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
  const handleNums1 = (e) => {
    setNums1Str(e.target.value.replace(/[^0-9,\s-]/g, "").replace(/,+/g, ","));
  };
  const handleNums2 = (e) => {
    setNums2Str(e.target.value.replace(/[^0-9,\s-]/g, "").replace(/,+/g, ","));
  };

  // Visualization rendering
  const renderNums = (nums, highlight, color) => (
    <div style={arrayRowStyle}>
      {nums.map((num, i) => (
        <div key={i} style={numBoxStyle(highlight === num, false, color)}>
          {num}
        </div>
      ))}
    </div>
  );
  const renderResult = (arr, label) => (
    <div style={{ display: "flex", alignItems: "center", gap: "0.25rem", margin: "0.15rem 0" }}>
      <span style={{ fontSize: "0.85rem", color: "#888", marginRight: 2 }}>{label}:</span>
      {arr.length === 0 ? (
        <span style={{ color: "#aaa", fontSize: "0.95rem" }}>[]</span>
      ) : (
        arr.map((n, i) => (
          <span key={i} style={resultBoxStyle}>
            {n}
          </span>
        ))
      )}
    </div>
  );

  let highlight1 = null,
    highlight2 = null;
  if (step.type === "diff1") highlight1 = step.current;
  if (step.type === "diff2") highlight2 = step.current;

  return (
    <div style={containerStyle}>
      <div style={cardStyle(isDesktop)}>
        {/* Left Column: Inputs and Controls */}
        <div style={leftColStyle(isDesktop)}>
          <div>
            <div style={labelStyle}>nums1 (comma-separated)</div>
            <input style={inputStyle} value={nums1Str} onChange={handleNums1} maxLength={100} autoComplete="off" spellCheck={false} />
          </div>
          <div>
            <div style={labelStyle}>nums2 (comma-separated)</div>
            <input style={inputStyle} value={nums2Str} onChange={handleNums2} maxLength={100} autoComplete="off" spellCheck={false} />
          </div>
          <div>
            <div style={labelStyle}>Speed: {speed.toFixed(2)}s/step</div>
            <input style={{ width: "100%" }} type="range" min={0.3} max={2.5} step={0.01} value={speed} onChange={handleSpeed} />
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
              style={{ background: "none", border: "none", padding: 2, cursor: "pointer", borderRadius: 6, outline: "none" }}
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
              style={{ background: "none", border: "none", padding: 2, cursor: "pointer", borderRadius: 6, outline: "none" }}
              onClick={handleReset}
              onMouseEnter={() => setHoverBtn("reset")}
              onMouseLeave={() => setHoverBtn("")}
              aria-label="Reset"
            >
              <ResetIcon color={hoverBtn === "reset" ? "#0051a8" : "#007aff"} />
            </button>
          </div>
          <input style={sliderStyle} type="range" min={0} max={maxStep} value={currentStep} onChange={handleSlider} />
          <div style={{ fontSize: "0.75rem", color: "#888", textAlign: "center" }}>
            Step {currentStep + 1} / {steps.length}
          </div>
        </div>
        {/* Right Column: Visualization and Action */}
        <div style={rightColStyle(isDesktop)}>
          <div style={visAreaStyle}>
            <div style={{ fontSize: "0.85rem", fontWeight: 500, marginBottom: 2 }}>nums1</div>
            {renderNums(step.nums1, highlight1, "#007aff")}
            <div style={{ fontSize: "0.85rem", fontWeight: 500, margin: "0.25rem 0 2px 0" }}>nums2</div>
            {renderNums(step.nums2, highlight2, "#ff9500")}
            {renderResult(step.diff1, "nums1 - nums2")}
            {renderResult(step.diff2, "nums2 - nums1")}
          </div>
          <div style={actionBoxStyle}>
            <span style={{ fontWeight: 600, marginRight: 6 }}>Current Action:</span> {step.message}
          </div>
        </div>
      </div>
    </div>
  );
};

export default FindDifferenceOfTwoArraysVisualizer;
