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

// Helper: Parse edges input
function parseEdges(str) {
  return str
    .split(/\n|;/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => line.split(/,|\s+/).map(Number))
    .filter((arr) => arr.length === 3);
}

// Main Visualizer Component
const Problem3608Visualizer = () => {
  // Default example
  const [n, setN] = useState(3);
  const [edgesInput, setEdgesInput] = useState("0,1,2\n1,2,4");
  const [k, setK] = useState(3);
  const [edges, setEdges] = useState([
    [0, 1, 2],
    [1, 2, 4],
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

  // Parse edges input
  useEffect(() => {
    try {
      const parsed = parseEdges(edgesInput);
      setEdges(parsed);
    } catch {}
  }, [edgesInput]);

  // Generate visualization steps
  const steps = useMemo(() => generateVisualization(n, edges, k), [n, edges, k]);
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
            <div style={{fontSize: "0.9rem", fontWeight: 600, marginBottom: 4}}>n (nodes)</div>
            <input type="number" min={1} max={10} value={n} onChange={(e) => setN(Number(e.target.value))} style={inputStyle} />
          </div>
          <div>
            <div style={{fontSize: "0.9rem", fontWeight: 600, marginBottom: 4}}>edges (u,v,time)</div>
            <textarea
              rows={isDesktop ? 4 : 2}
              value={edgesInput}
              onChange={(e) => setEdgesInput(e.target.value)}
              style={{...inputStyle, width: "100%", fontFamily: "monospace", fontSize: "0.95rem", resize: "vertical"}}
            />
          </div>
          <div>
            <div style={{fontSize: "0.9rem", fontWeight: 600, marginBottom: 4}}>k (components)</div>
            <input type="number" min={1} max={n} value={k} onChange={(e) => setK(Number(e.target.value))} style={inputStyle} />
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
                Time: <b>O(E log T)</b>
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
          <div style={{fontWeight: 700, fontSize: "1.1rem", marginBottom: 2}}>Minimum Time for K Connected Components</div>
          <GraphVisualization {...step} n={n} k={k} />
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
function generateVisualization(n, edges, k) {
  // Sort edges by time
  const edgesByTime = [...edges].sort((a, b) => a[2] - b[2]);
  const times = Array.from(new Set(edgesByTime.map((e) => e[2]))).sort((a, b) => a - b);
  let lo = 0,
    hi = times.length ? times[times.length - 1] : 0;
  let steps = [];
  // Initial components
  const initialComps = countComponents(n, edgesByTime, -1);
  steps.push({
    type: "init",
    t: -1,
    comps: initialComps.comps,
    parent: initialComps.parent,
    removedEdges: [],
    message: `Initially, there are ${initialComps.comps.length} connected components.`,
    highlight: {t: -1, edges: []},
  });
  if (initialComps.comps.length >= k) {
    steps.push({
      type: "done",
      t: 0,
      comps: initialComps.comps,
      parent: initialComps.parent,
      removedEdges: [],
      message: `Already at least k=${k} components. Answer: 0`,
      highlight: {t: 0, edges: []},
      answer: 0,
    });
    return steps;
  }
  // Binary search simulation
  let left = 0,
    right = times.length - 1,
    answer = -1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const t = times[mid];
    const res = countComponents(n, edgesByTime, t);
    steps.push({
      type: "bs",
      t,
      comps: res.comps,
      parent: res.parent,
      removedEdges: edgesByTime.filter((e) => e[2] <= t),
      message: `Try t=${t}: After removing edges with time ≤ ${t}, there are ${res.comps.length} components.`,
      highlight: {t, edges: edgesByTime.filter((e) => e[2] <= t)},
    });
    if (res.comps.length >= k) {
      answer = t;
      right = mid - 1;
      steps.push({
        type: "move-left",
        t,
        comps: res.comps,
        parent: res.parent,
        removedEdges: edgesByTime.filter((e) => e[2] <= t),
        message: `Number of components ≥ k (${k}). Try smaller t.`,
        highlight: {t, edges: edgesByTime.filter((e) => e[2] <= t)},
      });
    } else {
      left = mid + 1;
      steps.push({
        type: "move-right",
        t,
        comps: res.comps,
        parent: res.parent,
        removedEdges: edgesByTime.filter((e) => e[2] <= t),
        message: `Number of components < k (${k}). Try larger t.`,
        highlight: {t, edges: edgesByTime.filter((e) => e[2] <= t)},
      });
    }
  }
  // Final answer
  if (answer !== -1) {
    const res = countComponents(n, edgesByTime, answer);
    steps.push({
      type: "done",
      t: answer,
      comps: res.comps,
      parent: res.parent,
      removedEdges: edgesByTime.filter((e) => e[2] <= answer),
      message: `Found minimum t=${answer} with at least k=${k} components.`,
      highlight: {t: answer, edges: edgesByTime.filter((e) => e[2] <= answer)},
      answer,
    });
  } else {
    steps.push({
      type: "fail",
      t: null,
      comps: [],
      parent: [],
      removedEdges: [],
      message: `No such t found.`,
      highlight: {t: null, edges: []},
    });
  }
  return steps;
}

// Count components after removing edges with time <= t
function countComponents(n, edgesByTime, t) {
  const parent = Array.from({length: n}, (_, i) => i);
  function find(x) {
    while (parent[x] !== x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }
  function union(x, y) {
    const px = find(x),
      py = find(y);
    if (px !== py) parent[py] = px;
  }
  for (const [u, v, time] of edgesByTime) {
    if (time > t) union(u, v);
  }
  const comps = [];
  for (let i = 0; i < n; ++i) {
    if (find(i) === i) comps.push(i);
  }
  return {comps, parent};
}

// Graph Visualization
function GraphVisualization({n = 0, comps = [], parent = [], removedEdges = [], highlight = {}, t, k}) {
  // Build node positions in a circle
  if (!n || n < 1) return <div style={{minHeight: 120, color: "#888"}}>No nodes to display.</div>;
  const R = 60 + 12 * Math.max(0, n - 4);
  const centerX = 90,
    centerY = 90;
  const angle = n > 1 ? (2 * Math.PI) / n : 0;
  const nodePos = Array.from({length: n}, (_, i) => [
    centerX + R * Math.cos(i * angle - Math.PI / 2),
    centerY + R * Math.sin(i * angle - Math.PI / 2),
  ]);
  // Color by component
  const compMap = {};
  comps.forEach((c, idx) => {
    compMap[c] = idx;
  });
  // Edges
  const edgeLines = ((parentArr) => {
    const lines = [];
    for (let i = 0; i < n; ++i) {
      if (parentArr[i] !== i && nodePos[i] && nodePos[parentArr[i]]) {
        lines.push([i, parentArr[i]]);
      }
    }
    return lines;
  })(parent);
  // Removed edges
  const removedSet = new Set((removedEdges || []).map((e) => `${e[0]}-${e[1]}`));
  // Render
  return (
    <svg width={180} height={180} style={{background: "#f7f7f8", border: "1px solid #e5e5e5", borderRadius: 8, margin: "0 auto", display: "block"}}>
      {/* Draw remaining edges */}
      {edgeLines.map(([u, v], idx) =>
        nodePos[u] && nodePos[v] ? (
          <line key={idx} x1={nodePos[u][0]} y1={nodePos[u][1]} x2={nodePos[v][0]} y2={nodePos[v][1]} stroke="#007aff" strokeWidth={2} />
        ) : null
      )}
      {/* Draw removed edges (dashed) */}
      {(removedEdges || []).map(([u, v, time], idx) =>
        nodePos[u] && nodePos[v] ? (
          <line
            key={"r" + idx}
            x1={nodePos[u][0]}
            y1={nodePos[u][1]}
            x2={nodePos[v][0]}
            y2={nodePos[v][1]}
            stroke="#888"
            strokeWidth={1.5}
            strokeDasharray="4 3"
          />
        ) : null
      )}
      {/* Draw nodes */}
      {nodePos.map(([x, y], i) =>
        typeof x === "number" && typeof y === "number" ? (
          <g key={i}>
            <circle cx={x} cy={y} r={15} fill={comps.length ? compColor(compMap[findRoot(i, parent)]) : "#fff"} stroke="#007aff" strokeWidth={2} />
            <text x={x} y={y + 5} textAnchor="middle" fontSize={14} fontWeight={600} fill="#222">
              {i}
            </text>
          </g>
        ) : null
      )}
    </svg>
  );
}
function findRoot(i, parent) {
  while (parent[i] !== i) i = parent[i];
  return i;
}
function compColor(idx) {
  const palette = ["#f7b731", "#20bf6b", "#eb3b5a", "#8854d0", "#3867d6", "#fa8231", "#0fb9b1", "#fd9644", "#a55eea", "#4b6584"];
  return palette[idx % palette.length];
}

export default Problem3608Visualizer;
