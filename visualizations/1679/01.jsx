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

const defaultNums = "1,2,3,4";
const defaultK = 5;

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
  width: isDesktop ? 700 : "98vw",
  maxWidth: "99vw",
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
const numBoxStyle = (active, paired, faded) => ({
  border: "1.5px solid",
  borderColor: paired ? "#00b894" : active ? "#007aff" : "#e5e5e5",
  background: paired ? "#eafbe7" : active ? "#eaf4ff" : faded ? "#f7f7f8" : "#fff",
  color: "#222",
  borderRadius: "0.4rem",
  padding: "0.25rem 0.6rem",
  fontWeight: 600,
  fontSize: "1.1rem",
  minWidth: "2.1rem",
  textAlign: "center",
  transform: active || paired ? "scale(1.12)" : "none",
  transition: "all 0.2s",
  opacity: faded ? 0.5 : 1,
});
const pairRowStyle = {
  display: "flex",
  gap: "0.5rem",
  alignItems: "center",
  margin: "0.15rem 0",
};
const hashMapBoxStyle = {
  border: "1px solid #e5e5e5",
  background: "#fafbfc",
  borderRadius: "0.4rem",
  padding: "0.25rem 0.5rem",
  fontWeight: 500,
  fontSize: "0.95rem",
  minWidth: "2.2rem",
  textAlign: "center",
  margin: "0 0.1rem",
};

function parseNums(str) {
  return str
    .split(",")
    .map((s) => parseInt(s.trim(), 10))
    .filter((x) => !isNaN(x));
}

function generateVisualization(numsStr, k) {
  const nums = parseNums(numsStr);
  const steps = [];
  const n = nums.length;
  let count = {};
  let used = Array(n).fill(false);
  let pairs = [];
  let opCount = 0;
  // Initial step
  steps.push({
    type: "initial",
    nums: [...nums],
    k,
    count: {...count},
    used: [...used],
    pairs: [...pairs],
    opCount,
    idx: null,
    message: "Start with the input array and empty hash map.",
  });
  for (let i = 0; i < n; ++i) {
    const x = nums[i];
    const y = k - x;
    // Check for complement
    if (count[y] > 0) {
      // Pair found
      steps.push({
        type: "pair",
        nums: [...nums],
        k,
        count: {...count},
        used: used.map((u, idx) => (idx === i || (nums[idx] === y && !u) ? true : u)),
        pairs: [...pairs, [y, x]],
        opCount: opCount + 1,
        idx: i,
        pairIdx: nums.findIndex((val, idx2) => val === y && !used[idx2]),
        message: `nums[${i}] = ${x}. Found complement ${y} in hash map. Pair (${y}, ${x}) and remove both.`,
      });
      // Mark both as used
      used[i] = true;
      const pairIdx = nums.findIndex((val, idx2) => val === y && !used[idx2]);
      if (pairIdx !== -1) used[pairIdx] = true;
      count[y]--;
      pairs.push([y, x]);
      opCount++;
    } else {
      // No pair, add to hash map
      steps.push({
        type: "add",
        nums: [...nums],
        k,
        count: {...count, [x]: (count[x] || 0) + 1},
        used: [...used],
        pairs: [...pairs],
        opCount,
        idx: i,
        message: `nums[${i}] = ${x}. No complement ${y} found. Add ${x} to hash map.`,
      });
      count[x] = (count[x] || 0) + 1;
    }
  }
  // Final step
  steps.push({
    type: "final",
    nums: [...nums],
    k,
    count: {...count},
    used: [...used],
    pairs: [...pairs],
    opCount,
    idx: null,
    message: `Done! Maximum number of operations: ${opCount}.`,
  });
  return steps;
}

const MaxNumberOfKSumPairsVisualizer = () => {
  const [numsStr, setNumsStr] = useState(defaultNums);
  const [k, setK] = useState(defaultK);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1.2); // seconds per step
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hoverBtn, setHoverBtn] = useState("");
  const steps = useMemo(() => generateVisualization(numsStr, k), [numsStr, k]);
  const maxStep = steps.length - 1;

  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth >= 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    setCurrentStep(0);
    setIsPlaying(false);
  }, [numsStr, k]);

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
  const nums = parseNums(step.nums.join(","));

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
  const handleNums = (e) => {
    setNumsStr(e.target.value.replace(/[^0-9,\s-]/g, "").replace(/,+/g, ","));
  };
  const handleK = (e) => {
    let val = parseInt(e.target.value, 10);
    if (isNaN(val)) val = "";
    setK(val);
  };

  // Visualization rendering
  const renderNums = (nums, used, idx, pairIdx) => (
    <div style={arrayRowStyle}>
      {nums.map((num, i) => (
        <div key={i} style={numBoxStyle(i === idx, step.type === "pair" && (i === idx || i === pairIdx), used[i])}>
          {num}
        </div>
      ))}
    </div>
  );
  const renderPairs = (pairs) => (
    <div style={{margin: "0.25rem 0", width: "100%"}}>
      <div style={{fontSize: "0.85rem", fontWeight: 500, marginBottom: 2}}>Pairs found:</div>
      {pairs.length === 0 ? (
        <div style={{fontSize: "0.85rem", color: "#888"}}>None yet</div>
      ) : (
        pairs.map((p, i) => (
          <div key={i} style={pairRowStyle}>
            <span style={numBoxStyle(false, true, false)}>{p[0]}</span>
            <span style={{fontSize: "1.2rem", color: "#888"}}>+</span>
            <span style={numBoxStyle(false, true, false)}>{p[1]}</span>
            <span style={{fontSize: "1.1rem", color: "#00b894", fontWeight: 600}}>= {step.k}</span>
          </div>
        ))
      )}
    </div>
  );
  const renderHashMap = (count) => (
    <div style={{margin: "0.25rem 0", width: "100%"}}>
      <div style={{fontSize: "0.85rem", fontWeight: 500, marginBottom: 2}}>Hash Map (number: count):</div>
      <div style={arrayRowStyle}>
        {Object.keys(count).length === 0 ? (
          <span style={{color: "#888", fontSize: "0.85rem"}}>Empty</span>
        ) : (
          Object.entries(count).map(([num, cnt], i) => (
            <span key={i} style={hashMapBoxStyle}>
              {num}: {cnt}
            </span>
          ))
        )}
      </div>
    </div>
  );

  return (
    <div style={containerStyle}>
      <div style={cardStyle(isDesktop)}>
        {/* Left Column: Inputs and Controls */}
        <div style={leftColStyle(isDesktop)}>
          <div>
            <div style={labelStyle}>nums (comma-separated)</div>
            <input style={inputStyle} value={numsStr} onChange={handleNums} maxLength={100} autoComplete="off" spellCheck={false} />
          </div>
          <div>
            <div style={labelStyle}>k</div>
            <input style={inputStyle} value={k} onChange={handleK} type="number" min={1} max={1000000000} />
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
            <div style={{fontSize: "0.85rem", fontWeight: 500, marginBottom: 2}}>nums</div>
            {renderNums(nums, step.used, step.idx, step.pairIdx)}
            {renderPairs(step.pairs)}
            {renderHashMap(step.count)}
            <div style={{fontSize: "0.85rem", fontWeight: 500, margin: "0.25rem 0 2px 0"}}>
              Total operations: <span style={{color: "#007aff", fontWeight: 700}}>{step.opCount}</span>
            </div>
          </div>
          <div style={actionBoxStyle}>
            <span style={{fontWeight: 600, marginRight: 6}}>Current Action:</span> {step.message}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MaxNumberOfKSumPairsVisualizer;
