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

// Helper: Deep copy 2D array
const deepCopy2D = (arr) => arr.map((row) => [...row]);

// Main Visualizer Component
const Problem3603Visualizer = () => {
  // Default example
  const [m, setM] = useState(2);
  const [n, setN] = useState(3);
  const [waitCost, setWaitCost] = useState([
    [6, 1, 4],
    [3, 2, 5],
  ]);
  // For editing waitCost
  const [waitCostInput, setWaitCostInput] = useState("6,1,4\n3,2,5");

  // Visualization state
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(900);
  const [isDesktop, setIsDesktop] = useState(true);
  const timerRef = useRef();

  // Time/space simulation
  const [tCount, setTCount] = useState(0); // Simulate O(mn) steps

  // Responsive layout
  useEffect(() => {
    const handleResize = () => setIsDesktop(window.innerWidth >= 768);
    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // Parse waitCost input
  useEffect(() => {
    try {
      const rows = waitCostInput
        .trim()
        .split(/\n|;/)
        .map((row) => row.split(/,|\s+/).map(Number));
      if (rows.length && rows[0].length) {
        setWaitCost(rows);
        setM(rows.length);
        setN(rows[0].length);
      }
    } catch {}
  }, [waitCostInput]);

  // Generate visualization steps
  const steps = useMemo(() => generateVisualization(m, n, waitCost), [m, n, waitCost]);
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
            <div style={{fontSize: "0.9rem", fontWeight: 600, marginBottom: 4}}>Grid Size</div>
            <div style={{display: "flex", gap: 8}}>
              <label style={{fontSize: "0.85rem"}}>
                m: <input type="number" min={1} max={10} value={m} onChange={(e) => setM(Number(e.target.value))} style={inputStyle} />
              </label>
              <label style={{fontSize: "0.85rem"}}>
                n: <input type="number" min={1} max={10} value={n} onChange={(e) => setN(Number(e.target.value))} style={inputStyle} />
              </label>
            </div>
          </div>
          <div>
            <div style={{fontSize: "0.9rem", fontWeight: 600, marginBottom: 4}}>waitCost (comma/space/line separated)</div>
            <textarea
              rows={isDesktop ? 4 : 2}
              value={waitCostInput}
              onChange={(e) => setWaitCostInput(e.target.value)}
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
          {/* Time/Space Complexity Block */}
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
            <div style={{display: "flex", gap: 12, alignItems: "center"}}>
              <span>
                Time: <b>O(mn)</b>
              </span>
              <span>
                Space: <b>O(mn)</b>
              </span>
              <span style={{color: "#007aff", fontWeight: 600}}>t = {tCount}</span>
            </div>
          </div>
        </div>
        {/* Right Column: Visualization & Message */}
        <div style={{flex: 2, minWidth: 0, display: "flex", flexDirection: "column", gap: "1rem"}}>
          <div style={{fontWeight: 700, fontSize: "1.1rem", marginBottom: 2}}>Minimum Cost Path with Alternating Directions II</div>
          <GridVisualization {...step} m={m} n={n} waitCost={waitCost} />
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
function generateVisualization(m, n, waitCost) {
  // DP: cost[i][j][parity] (0=wait, 1=move)
  const steps = [];
  const cost = Array.from({length: m}, () => Array.from({length: n}, () => [Infinity, Infinity]));
  cost[0][0][1] = 1; // Start at (0,0), move step, cost=1
  steps.push({
    type: "init",
    cost: deepCopy2D(cost),
    pos: [0, 0],
    parity: 1,
    message: "Start at (0,0) with entry cost 1 (move step).",
    path: [[0, 0]],
    action: "init",
  });
  const queue = [[0, 0, 1]]; // i, j, parity
  const prev = Array.from({length: m}, () => Array.from({length: n}, () => [null, null]));
  let stepCount = 1;
  while (queue.length) {
    const [i, j, parity] = queue.shift();
    const currCost = cost[i][j][parity];
    steps.push({
      type: parity ? "move" : "wait",
      cost: deepCopy2D(cost),
      pos: [i, j],
      parity,
      message: parity
        ? `At (${i},${j}) on move step. Try moving right or down.`
        : `At (${i},${j}) on wait step. Must wait in place, paying waitCost[${i}][${j}] = ${waitCost[i][j]}.`,
      path: reconstructPath(prev, i, j, parity),
      action: parity ? "move" : "wait",
    });
    if (parity === 1) {
      // Move step: right or down
      for (const [di, dj] of [
        [0, 1],
        [1, 0],
      ]) {
        const ni = i + di,
          nj = j + dj;
        if (ni < m && nj < n) {
          const entryCost = (ni + 1) * (nj + 1);
          if (currCost + entryCost < cost[ni][nj][0]) {
            cost[ni][nj][0] = currCost + entryCost;
            prev[ni][nj][0] = [i, j, 1];
            queue.push([ni, nj, 0]);
            steps.push({
              type: "move-to",
              cost: deepCopy2D(cost),
              pos: [ni, nj],
              parity: 0,
              message: `Move to (${ni},${nj}), pay entry cost ${(ni + 1) * (nj + 1)}. Next: wait step.`,
              path: reconstructPath(prev, ni, nj, 0),
              action: "move-to",
            });
          }
        }
      }
    } else {
      // Wait step: stay in place
      if (currCost + waitCost[i][j] < cost[i][j][1]) {
        cost[i][j][1] = currCost + waitCost[i][j];
        prev[i][j][1] = [i, j, 0];
        queue.push([i, j, 1]);
        steps.push({
          type: "wait-done",
          cost: deepCopy2D(cost),
          pos: [i, j],
          parity: 1,
          message: `Wait at (${i},${j}), pay waitCost[${i}][${j}] = ${waitCost[i][j]}. Next: move step.`,
          path: reconstructPath(prev, i, j, 1),
          action: "wait-done",
        });
      }
    }
    stepCount++;
    if (stepCount > m * n * 4) break; // Safety for visualization
  }
  // Find min cost at end
  const minCost = Math.min(cost[m - 1][n - 1][0], cost[m - 1][n - 1][1]);
  steps.push({
    type: "final",
    cost: deepCopy2D(cost),
    pos: [m - 1, n - 1],
    parity: cost[m - 1][n - 1][0] <= cost[m - 1][n - 1][1] ? 0 : 1,
    message: `Arrived at (${m - 1},${n - 1}). Minimum total cost: ${minCost}.`,
    path: reconstructPath(prev, m - 1, n - 1, cost[m - 1][n - 1][0] <= cost[m - 1][n - 1][1] ? 0 : 1),
    minCost,
    action: "final",
  });
  return steps;
}

function reconstructPath(prev, i, j, parity) {
  const path = [];
  while (i !== null && j !== null && parity !== null) {
    path.push([i, j]);
    const p = prev[i][j][parity];
    if (!p) break;
    [i, j, parity] = p;
  }
  return path.reverse();
}

// Grid Visualization
function GridVisualization({cost = [], pos = [0, 0], parity = 1, path = [], m, n, waitCost = [], minCost, action}) {
  // Render grid
  return (
    <div style={{display: "inline-block", background: "#f7f7f8", border: "1px solid #e5e5e5", borderRadius: 8, padding: "0.5rem", minWidth: 120}}>
      <table style={{borderCollapse: "collapse", margin: "0 auto"}}>
        <tbody>
          {Array.from({length: m}).map((_, i) => (
            <tr key={i}>
              {Array.from({length: n}).map((_, j) => {
                const isCurrent = pos[0] === i && pos[1] === j;
                const isPath = path.some(([pi, pj]) => pi === i && pj === j);
                return (
                  <td
                    key={j}
                    style={{
                      border: "1px solid #e5e5e5",
                      borderRadius: 4,
                      minWidth: 38,
                      height: 38,
                      textAlign: "center",
                      verticalAlign: "middle",
                      background: isCurrent ? "#007aff22" : isPath ? "#007aff11" : "#fff",
                      fontWeight: isCurrent ? 700 : 500,
                      position: "relative",
                      transition: "background 0.2s",
                    }}
                  >
                    <div style={{fontSize: "0.85rem", color: "#333"}}>
                      <b>{(i + 1) * (j + 1)}</b>
                    </div>
                    <div style={{fontSize: "0.7rem", color: "#888"}}>wait: {waitCost[i]?.[j]}</div>
                    {isCurrent && <div style={{position: "absolute", top: 2, right: 4, fontSize: 11, color: "#007aff", fontWeight: 700}}>●</div>}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
      {typeof minCost === "number" && <div style={{marginTop: 8, fontSize: "0.95rem", fontWeight: 600, color: "#007aff"}}>Min Cost: {minCost}</div>}
    </div>
  );
}

export default Problem3603Visualizer;
