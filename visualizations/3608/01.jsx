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

// --- Helper: Union-Find (DSU) ---
function createDSU(n) {
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
  function getComponents() {
    const roots = new Set();
    for (let i = 0; i < n; ++i) roots.add(find(i));
    return Array.from(roots);
  }
  return {parent, find, union, getComponents};
}

// --- Main Visualizer Component ---
export default function MinimumTimeForKConnectedComponentsVisualizer() {
  // --- State Management ---
  const [n, setN] = useState(3);
  const [edges, setEdges] = useState([
    [0, 1, 2],
    [1, 2, 4],
  ]);
  const [k, setK] = useState(3);
  const [inputN, setInputN] = useState("3");
  const [inputEdges, setInputEdges] = useState("0,1,2\n1,2,4");
  const [inputK, setInputK] = useState("3");
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1200);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hover, setHover] = useState({prev: false, play: false, next: false, reset: false});

  // --- Visualization Logic ---
  const generateVisualization = useMemo(() => {
    return (n, edges, k) => {
      const steps = [];
      if (k === n) {
        steps.push({
          type: "final",
          message: `k = n, so answer is 0.`,
          t: 0,
          comps: n,
          parent: Array.from({length: n}, (_, i) => i),
          lo: 0,
          hi: 0,
          mid: 0,
        });
        return {steps};
      }
      if (!edges.length) {
        steps.push({
          type: "final",
          message: `No edges. If k <= n, answer is 0.`,
          t: 0,
          comps: n,
          parent: Array.from({length: n}, (_, i) => i),
          lo: 0,
          hi: 0,
          mid: 0,
        });
        return {steps};
      }
      const times = Array.from(new Set(edges.map((e) => e[2]))).sort((a, b) => a - b);
      let lo = 0,
        hi = Math.max(...edges.map((e) => e[2]));
      let ans = hi;
      let binarySteps = [];
      // Binary search simulation
      while (lo <= hi) {
        let mid = Math.floor((lo + hi) / 2);
        // DSU for this mid
        const dsu = createDSU(n);
        for (const [u, v, time] of edges) {
          if (time > mid) dsu.union(u, v);
        }
        const comps = dsu.getComponents().length;
        binarySteps.push({
          type: "binary_search",
          t: mid,
          comps,
          parent: [...dsu.parent],
          lo,
          hi,
          mid,
          message: `t = ${mid}: After removing edges with time <= t, components = ${comps}. (lo=${lo}, hi=${hi})`,
        });
        if (comps >= k) {
          ans = mid;
          hi = mid - 1;
        } else {
          lo = mid + 1;
        }
      }
      steps.push(...binarySteps);
      steps.push({type: "final", message: `Done. Minimum time t = ${ans}.`, t: ans, comps: null, parent: null, lo: null, hi: null, mid: null});
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
    const {steps} = generateVisualization(n, edges, k);
    setVisualizationSteps(steps);
    setCurrentStep(0);
    setIsPlaying(false);
  }, [n, edges, k, generateVisualization]);

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
  const handleInputN = (e) => {
    setInputN(e.target.value);
    const val = parseInt(e.target.value, 10);
    if (!isNaN(val) && val > 0) setN(val);
  };
  const handleInputEdges = (e) => {
    setInputEdges(e.target.value);
    const arr = e.target.value
      .split(/\n|;/)
      .map((line) => line.split(",").map((x) => parseInt(x.trim(), 10)))
      .filter((arr) => arr.length === 3 && arr.every((x) => !isNaN(x)));
    setEdges(arr);
  };
  const handleInputK = (e) => {
    setInputK(e.target.value);
    const val = parseInt(e.target.value, 10);
    if (!isNaN(val) && val > 0) setK(val);
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
    maxWidth: 900,
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
    minHeight: 120,
    width: "100%",
    marginBottom: 12,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  };
  const nodesRow = {display: "flex", gap: 8, margin: "0.5rem 0"};
  const nodeStyle = (active, comp) => ({
    padding: "0.5rem 0.9rem",
    borderRadius: 6,
    border: `2px solid ${active ? palette.primary : palette.border}`,
    background: comp !== undefined ? `hsl(${(comp * 67) % 360}, 80%, 92%)` : "#fff",
    color: palette.text,
    fontWeight: active ? 700 : 500,
    fontSize: 18,
    transform: active ? "scale(1.12)" : "none",
    transition: "all 0.2s",
  });
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
  const searchBox = {
    margin: "0.5rem 0",
    padding: "0.25rem 0.5rem",
    border: `1px solid ${palette.primary}`,
    borderRadius: 6,
    background: "#f7fbff",
    fontSize: 15,
    fontWeight: 600,
    color: palette.primary,
    display: "inline-block",
  };

  // --- Visualization Frame Renderer ---
  const renderFrame = () => {
    const step = visualizationSteps[currentStep] || {};
    const {t, comps, parent, lo, hi, mid, type} = step;
    let compMap = {};
    if (parent) {
      // Map each node to its component root
      for (let i = 0; i < parent.length; ++i) {
        let x = i;
        while (parent[x] !== x) x = parent[x];
        compMap[i] = x;
      }
    }
    return (
      <div style={vizArea}>
        <div style={{fontSize: 15, marginBottom: 6}}>Nodes:</div>
        <div style={nodesRow}>
          {Array.from({length: n}, (_, idx) => (
            <div key={idx} style={nodeStyle(false, compMap[idx])}>
              {idx}
            </div>
          ))}
        </div>
        {typeof t === "number" && (
          <div style={{margin: "0.5rem 0 0.25rem 0"}}>
            <span style={searchBox}>Current t = {t}</span>
            {typeof comps === "number" && <span style={{marginLeft: 16, color: palette.primary, fontWeight: 500}}>Components = {comps}</span>}
          </div>
        )}
        {typeof lo === "number" && typeof hi === "number" && (
          <div style={{fontSize: 13, color: "#888", margin: "0.25rem 0"}}>
            Binary search: lo = {lo}, hi = {hi}, mid = {mid}
          </div>
        )}
      </div>
    );
  };

  // --- Main Render ---
  return (
    <div style={{background: palette.background, minHeight: "100vh", padding: 0}}>
      <div style={cardStyle}>
        {/* Left Column: Inputs & Controls */}
        <div style={leftCol}>
          <div style={{fontWeight: 600, fontSize: 18, marginBottom: 8}}>Minimum Time for K Connected Components</div>
          <div style={{fontSize: 14, marginBottom: 4}}>n (number of nodes):</div>
          <input type="number" min={1} value={inputN} onChange={handleInputN} style={inputStyle} />
          <div style={{fontSize: 14, marginBottom: 4}}>edges (u,v,time) per line:</div>
          <textarea value={inputEdges} onChange={handleInputEdges} style={{...inputStyle, minHeight: 60, fontFamily: "monospace"}} />
          <div style={{fontSize: 14, marginBottom: 4}}>k (components):</div>
          <input type="number" min={1} value={inputK} onChange={handleInputK} style={inputStyle} />
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
