import React, {useState, useMemo, useEffect, useRef} from "react";

// SVG ICONS
const PlayIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M6 4L15 10L6 16V4Z" fill={color} />
  </svg>
);
const PauseIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <rect x="5" y="4" width="3" height="12" rx="1" fill={color} />
    <rect x="12" y="4" width="3" height="12" rx="1" fill={color} />
  </svg>
);
const PrevIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M13 16L7 10L13 4" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);
const NextIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M7 4L13 10L7 16" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);
const ResetIcon = ({color = "#007aff"}) => (
  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path
      d="M10 4V1L5 6l5 5V7c2.76 0 5 2.24 5 5 0 2.76-2.24 5-5 5s-5-2.24-5-5"
      stroke={color}
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

// Helper: Parse points input
function parsePoints(str) {
  return str
    .split(/\n|;/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => line.replace(/\[|\]/g, "").split(/,|\s+/).map(Number))
    .filter((arr) => arr.length === 2);
}

// Main Visualizer Component
const Problem3623Visualizer = () => {
  // Default example
  const [pointsInput, setPointsInput] = useState("1,0\n2,0\n3,0\n2,2\n3,2");
  const [points, setPoints] = useState([
    [1, 0],
    [2, 0],
    [3, 0],
    [2, 2],
    [3, 2],
  ]);

  // Visualization state
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(900);
  const [isDesktop, setIsDesktop] = useState(true);
  const timerRef = useRef();
  const [tCount, setTCount] = useState(0); // Complexity simulation

  // Responsive layout
  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth >= 768);
    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // Parse points input
  useEffect(() => {
    try {
      const parsed = parsePoints(pointsInput);
      setPoints(parsed);
    } catch {}
  }, [pointsInput]);

  // Generate visualization steps
  const steps = useMemo(() => generateVisualization(points), [points]);
  useEffect(() => {
    setVisualizationSteps(steps);
    setCurrentStep(0);
    setTCount(0);
  }, [steps]);

  // Playback logic
  useEffect(() => {
    if (isPlaying && currentStep < visualizationSteps.length - 1) {
      timerRef.current = setTimeout(() => {
        setCurrentStep((s) => s + 1);
        setTCount((t) => t + 1);
      }, speed);
    } else {
      clearTimeout(timerRef.current);
    }
    return () => clearTimeout(timerRef.current);
  }, [isPlaying, currentStep, visualizationSteps.length, speed]);

  // Controls
  const goToStep = (idx) => {
    setCurrentStep(idx);
    setTCount(idx);
    setIsPlaying(false);
  };
  const handlePrev = () => goToStep(Math.max(0, currentStep - 1));
  const handleNext = () => goToStep(Math.min(visualizationSteps.length - 1, currentStep + 1));
  const handleReset = () => goToStep(0);
  const handlePlayPause = () => setIsPlaying((p) => !p);

  // Render
  const step = visualizationSteps[currentStep] || {};

  return (
    <div style={{background: "#fff", minHeight: 0, padding: 0, margin: 0}}>
      <div
        style={{
          maxWidth: 900,
          margin: "2rem auto",
          boxShadow: "0 2px 16px #e5e5e5",
          borderRadius: 12,
          background: "#fff",
          padding: isDesktop ? "1.5rem" : "0.5rem",
          display: "flex",
          flexDirection: isDesktop ? "row" : "column",
          gap: "1.5rem",
        }}
      >
        {/* Left Column: Inputs & Controls */}
        <div style={{flex: 1, minWidth: 220, maxWidth: 320, display: "flex", flexDirection: "column", gap: "1.5rem"}}>
          <div>
            <div style={{fontSize: "0.9rem", fontWeight: 600, marginBottom: 4}}>points (x,y)</div>
            <textarea
              rows={isDesktop ? 6 : 3}
              value={pointsInput}
              onChange={(e) => setPointsInput(e.target.value)}
              style={{...inputStyle, width: "100%", fontFamily: "monospace", fontSize: "0.95rem", resize: "vertical"}}
            />
          </div>
          <div>
            <div style={{fontSize: "0.9rem", fontWeight: 600, marginBottom: 4}}>Controls</div>
            <div style={{display: "flex", gap: 8, alignItems: "center"}}>
              <button style={buttonStyle} onClick={handlePrev} disabled={currentStep === 0}>
                <PrevIcon />
              </button>
              <button style={buttonStyle} onClick={handlePlayPause}>
                {isPlaying ? <PauseIcon /> : <PlayIcon />}
              </button>
              <button style={buttonStyle} onClick={handleNext} disabled={currentStep === visualizationSteps.length - 1}>
                <NextIcon />
              </button>
              <button style={buttonStyle} onClick={handleReset}>
                <ResetIcon />
              </button>
            </div>
            <input
              type="range"
              min={0}
              max={visualizationSteps.length - 1}
              value={currentStep}
              onChange={(e) => goToStep(Number(e.target.value))}
              style={{width: "100%", marginTop: 8}}
            />
          </div>
          {/* Complexity Block */}
          <div
            style={{
              background: "#f7f7f8",
              border: "1px solid #e5e5e5",
              borderRadius: 8,
              padding: "0.5rem 0.75rem",
              fontSize: "0.85rem",
              marginTop: 8,
            }}
          >
            <div style={{fontWeight: 600, fontSize: "0.8rem", marginBottom: 2}}>Complexity Simulation</div>
            <div style={{display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap"}}>
              <span>
                Time: <b>O(N + K²)</b>
              </span>
              <span>
                Space: <b>O(N)</b>
              </span>
              <span style={{color: "#007aff", fontWeight: 600}}>t = {tCount}</span>
            </div>
          </div>
        </div>
        {/* Right Column: Visualization & Message */}
        <div style={{flex: 2, minWidth: 0, display: "flex", flexDirection: "column", gap: "1rem"}}>
          <div style={{fontWeight: 700, fontSize: "1.1rem", marginBottom: 2}}>Count Number of Trapezoids I</div>
          <TrapezoidVisualization {...step} />
          <div
            style={{
              background: "#f7f7f8",
              border: "1px solid #e5e5e5",
              borderRadius: 8,
              padding: "0.5rem 0.75rem",
              fontSize: "0.95rem",
              minHeight: 36,
              display: "flex",
              alignItems: "center",
            }}
          >
            <span style={{fontWeight: 600, fontSize: "0.8rem", color: "#888", marginRight: 8}}>Current Action:</span>
            <span>{step.message}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

// Input styles
const inputStyle = {
  border: "1px solid #e5e5e5",
  borderRadius: 6,
  padding: "0.25rem 0.5rem",
  fontSize: "0.95rem",
  background: "#f7f7f8",
  width: 48,
  marginRight: 4,
};
const buttonStyle = {
  border: "none",
  background: "#f7f7f8",
  borderRadius: 6,
  padding: 6,
  cursor: "pointer",
  transition: "background 0.2s",
  outline: "none",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: 32,
  width: 32,
};

// Visualization logic
function generateVisualization(points) {
  const steps = [];
  // Step 1: Group by y
  const yMap = {};
  for (let i = 0; i < points.length; ++i) {
    const [x, y] = points[i];
    if (!yMap[y]) yMap[y] = [];
    yMap[y].push(x);
    steps.push({
      type: "group",
      yMap: JSON.parse(JSON.stringify(yMap)),
      message: `Add point (${x},${y}) to y=${y} group.`,
      highlight: {x, y},
      phase: "group",
    });
  }
  // Step 2: Compute C(c,2) for each y
  const c2 = [];
  const yLevels = Object.keys(yMap)
    .map(Number)
    .sort((a, b) => a - b);
  for (let i = 0; i < yLevels.length; ++i) {
    const y = yLevels[i];
    const c = yMap[y].length;
    const val = c >= 2 ? (c * (c - 1)) / 2 : 0;
    c2.push(val);
    steps.push({
      type: "c2",
      y,
      c,
      val,
      c2: [...c2],
      message: `For y=${y}, group size=${c}. Ways to pick 2: ${val}.`,
      highlight: {y},
      phase: "c2",
    });
  }
  // Step 3: Pairwise multiply
  let res = 0;
  for (let i = 0; i < c2.length; ++i) {
    for (let j = i + 1; j < c2.length; ++j) {
      const add = c2[i] * c2[j];
      res += add;
      steps.push({
        type: "pair",
        i,
        j,
        c2: [...c2],
        add,
        res,
        y1: yLevels[i],
        y2: yLevels[j],
        message: `Pair y=${yLevels[i]} and y=${yLevels[j]}: ${c2[i]} * ${c2[j]} = ${add}. Total so far: ${res}.`,
        highlight: {i, j},
        phase: "pair",
      });
    }
  }
  steps.push({
    type: "final",
    res,
    message: `Final result: ${res} trapezoids.`,
    phase: "final",
  });
  return steps;
}

// Visualization Area
function TrapezoidVisualization({type, yMap = {}, c2 = [], i, j, add, res, y, val, y1, y2, highlight, phase}) {
  // Show y-groups and C(c,2) table
  const yLevels = Object.keys(yMap)
    .map(Number)
    .sort((a, b) => a - b);
  return (
    <div style={{minHeight: 120}}>
      {/* Show y-groups */}
      <div style={{display: "flex", gap: 16, flexWrap: "wrap", marginBottom: 8}}>
        {yLevels.map((yy) => (
          <div key={yy} style={{background: "#f7f7f8", border: "1px solid #e5e5e5", borderRadius: 6, padding: "0.5rem 0.75rem", minWidth: 60}}>
            <div style={{fontWeight: 600, fontSize: "0.9rem", color: highlight && highlight.y === yy ? "#007aff" : "#333"}}>y={yy}</div>
            <div style={{display: "flex", gap: 4, flexWrap: "wrap"}}>
              {(yMap[yy] || []).map((xx, idx) => (
                <span
                  key={idx}
                  style={{
                    display: "inline-block",
                    background: highlight && highlight.x === xx && highlight.y === yy ? "#007aff22" : "#fff",
                    border: "1px solid #e5e5e5",
                    borderRadius: 4,
                    padding: "2px 6px",
                    margin: 1,
                    fontWeight: 500,
                    color: "#222",
                    fontSize: "0.95rem",
                  }}
                >
                  {xx}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
      {/* Show C(c,2) table */}
      {phase !== "group" && (
        <div style={{marginBottom: 8}}>
          <div style={{fontWeight: 600, fontSize: "0.9rem", marginBottom: 2}}>Ways to pick 2 from each y-level:</div>
          <div style={{display: "flex", gap: 12, flexWrap: "wrap"}}>
            {c2.map((v, idx) => (
              <span
                key={idx}
                style={{
                  background:
                    (phase === "c2" && highlight && highlight.y === yLevels[idx]) ||
                    (phase === "pair" && (highlight.i === idx || highlight.j === idx))
                      ? "#007aff22"
                      : "#fff",
                  border: "1px solid #e5e5e5",
                  borderRadius: 4,
                  padding: "2px 8px",
                  fontWeight: 600,
                  color: "#333",
                  fontSize: "0.95rem",
                }}
              >{`y=${yLevels[idx]}: ${v}`}</span>
            ))}
          </div>
        </div>
      )}
      {/* Show pairwise multiplication */}
      {phase === "pair" && (
        <div style={{fontSize: "0.98rem", marginBottom: 4}}>
          <span style={{color: "#007aff", fontWeight: 600}}>{`Pair: y=${y1} × y=${y2} → ${add}`}</span>
        </div>
      )}
      {/* Show final result */}
      {phase === "final" && <div style={{fontSize: "1.05rem", fontWeight: 700, color: "#007aff", marginTop: 8}}>Total trapezoids: {res}</div>}
    </div>
  );
}

export default Problem3623Visualizer;
