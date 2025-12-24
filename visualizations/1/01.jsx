import React, { useState, useEffect, useMemo, useCallback, useRef } from "react";

const TwoSumVisualizer = () => {
  const [nums, setNums] = useState([2, 7, 11, 15]);
  const [target, setTarget] = useState(9);
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hover, setHover] = useState(false);
  const timerRef = useRef(null);

  // Memoized generateVisualization function
  const generateVisualization = useMemo(() => {
    return (nums, target) => {
      const steps = [];
      const map = new Map();

      steps.push({ type: "initial", nums: [...nums], target, message: "Initialize the array and target." });

      for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        steps.push({
          type: "check_complement",
          index: i,
          value: nums[i],
          complement,
          map: new Map(map),
          message: `Checking if complement ${complement} exists for nums[${i}] = ${nums[i]}.`,
        });

        if (map.has(complement)) {
          const j = map.get(complement);
          steps.push({ type: "found", index1: j, index2: i, value1: nums[j], value2: nums[i], message: `Found the pair at indices ${j} and ${i}.` });
          return steps;
        }

        map.set(nums[i], i);
        steps.push({ type: "add_to_map", index: i, value: nums[i], map: new Map(map), message: `Adding nums[${i}] = ${nums[i]} to the map.` });
      }

      steps.push({ type: "not_found", message: "No solution found." });
      return steps;
    };
  }, []);

  useEffect(() => {
    setVisualizationSteps(generateVisualization(nums, target));
    setCurrentStep(0);
  }, [nums, target, generateVisualization]);

  useEffect(() => {
    const handleResize = () => {
      setIsDesktop(window.innerWidth >= 768);
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  useEffect(() => {
    if (isPlaying) {
      timerRef.current = setInterval(() => {
        setCurrentStep((prevStep) => (prevStep < visualizationSteps.length - 1 ? prevStep + 1 : 0));
      }, 1000 / speed);
    } else {
      clearInterval(timerRef.current);
    }
    return () => clearInterval(timerRef.current);
  }, [isPlaying, speed, visualizationSteps.length]);

  const handlePlayPause = useCallback(() => {
    setIsPlaying((prevIsPlaying) => !prevIsPlaying);
  }, []);

  const handleNext = useCallback(() => {
    setCurrentStep((prevStep) => (prevStep < visualizationSteps.length - 1 ? prevStep + 1 : prevStep));
  }, [visualizationSteps.length]);

  const handlePrevious = useCallback(() => {
    setCurrentStep((prevStep) => (prevStep > 0 ? prevStep - 1 : 0));
  }, []);

  const handleReset = useCallback(() => {
    setCurrentStep(0);
    setIsPlaying(false);
  }, []);

  const currentStepData = visualizationSteps[currentStep] || {};
  const totalSteps = visualizationSteps.length;

  const handleSliderChange = (event) => {
    setCurrentStep(parseInt(event.target.value, 10));
    setIsPlaying(false);
  };

  const PlayIcon = () => (
    <svg viewBox="0 0 24 24" style={{ height: "1.2rem", width: "1.2rem" }}>
      <path fill="currentColor" d="M6 4l12 8L6 20V4z" />
    </svg>
  );

  const PauseIcon = () => (
    <svg viewBox="0 0 24 24" style={{ height: "1.2rem", width: "1.2rem" }}>
      <path fill="currentColor" d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" />
    </svg>
  );

  const BackIcon = () => (
    <svg viewBox="0 0 24 24" style={{ height: "1.2rem", width: "1.2rem" }}>
      <path fill="currentColor" d="M11.67 3.87L9.9 2.1 0 12l9.9 9.9 1.77-1.77L3.54 12z" />
    </svg>
  );

  const ForwardIcon = () => (
    <svg viewBox="0 0 24 24" style={{ height: "1.2rem", width: "1.2rem" }}>
      <path fill="currentColor" d="M12.33 3.87L14.1 2.1 24 12l-9.9 9.9-1.77-1.77L20.46 12z" />
    </svg>
  );

  const ResetIcon = () => (
    <svg viewBox="0 0 24 24" style={{ height: "1.2rem", width: "1.2rem" }}>
      <path
        fill="currentColor"
        d="M13 3c-4.97 0-9 4.03-9 9H3l4 5 4-5H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06L9.29 16.29C10.86 17.86 12.85 18.67 15 18.67c4.97 0 9-4.03 9-9s-4.03-9-9-9z"
      />
    </svg>
  );

  return (
    <div
      style={{
        width: "100%",
        maxWidth: isDesktop ? "800px" : "100%",
        backgroundColor: "white",
        boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
        borderRadius: "8px",
        padding: "1rem",
        margin: "1rem",
      }}
    >
      <div style={{ display: isDesktop ? "flex" : "block", justifyContent: "space-between" }}>
        <div style={{ width: isDesktop ? "40%" : "100%", padding: "0.5rem" }}>
          <div style={{ marginBottom: "0.5rem" }}>
            <label htmlFor="nums" style={{ display: "block", fontSize: "0.875rem", marginBottom: "0.25rem" }}>
              Nums:
            </label>
            <input
              type="text"
              id="nums"
              style={{ width: "100%", padding: "0.5rem", borderRadius: "4px", border: "1px solid #e5e5e5" }}
              value={JSON.stringify(nums)}
              onChange={(e) => setNums(JSON.parse(e.target.value))}
            />
          </div>
          <div style={{ marginBottom: "0.5rem" }}>
            <label htmlFor="target" style={{ display: "block", fontSize: "0.875rem", marginBottom: "0.25rem" }}>
              Target:
            </label>
            <input
              type="number"
              id="target"
              style={{ width: "100%", padding: "0.5rem", borderRadius: "4px", border: "1px solid #e5e5e5" }}
              value={target}
              onChange={(e) => setTarget(parseInt(e.target.value))}
            />
          </div>

          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "0.5rem" }}>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{ backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px" }}
              onClick={handlePrevious}
              disabled={currentStep === 0}
            >
              <BackIcon />
            </button>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{ backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px" }}
              onClick={handlePlayPause}
            >
              {isPlaying ? <PauseIcon /> : <PlayIcon />}
            </button>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{ backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px" }}
              onClick={handleNext}
              disabled={currentStep === visualizationSteps.length - 1}
            >
              <ForwardIcon />
            </button>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{ backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px" }}
              onClick={handleReset}
            >
              <ResetIcon />
            </button>
          </div>
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "0.5rem" }}>
            <label htmlFor="animationSpeed" style={{ fontSize: "0.75rem" }}>
              Animation Speed:
            </label>
            <input
              type="number"
              id="animationSpeed"
              style={{ width: "60px", padding: "0.25rem", borderRadius: "4px", border: "1px solid #e5e5e5", fontSize: "0.75rem" }}
              value={speed}
              onChange={(e) => setSpeed(parseInt(e.target.value))}
            />
          </div>
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "0.5rem" }}>
            <span style={{ fontSize: "0.75rem" }}>
              Step {currentStep + 1} of {totalSteps}
            </span>
          </div>
          <input
            type="range"
            min="0"
            max={visualizationSteps.length - 1}
            value={currentStep}
            onChange={handleSliderChange}
            style={{ width: "100%" }}
          />
        </div>
        <div style={{ width: isDesktop ? "60%" : "100%", padding: "0.5rem", borderLeft: isDesktop ? "1px solid #e5e5e5" : "none" }}>
          <div
            style={{
              marginBottom: "0.5rem",
              fontSize: "0.75rem",
              backgroundColor: "#f7f7f7",
              padding: "0.25rem",
              border: "1px solid #e5e5e5",
              borderRadius: "4px",
            }}
          >
            {currentStepData.message}
          </div>

          {currentStepData.type === "initial" && (
            <div>
              <p>Array: {JSON.stringify(currentStepData.nums)}</p>
              <p>Target: {currentStepData.target}</p>
            </div>
          )}

          {currentStepData.type === "check_complement" && (
            <div>
              <p>
                Checking: nums[{currentStepData.index}] = {currentStepData.value}
              </p>
              <p>Complement: {currentStepData.complement}</p>
              <p>Map: {JSON.stringify(Array.from(currentStepData.map.entries()))}</p>
            </div>
          )}

          {currentStepData.type === "add_to_map" && (
            <div>
              <p>
                Adding to Map: nums[{currentStepData.index}] = {currentStepData.value}
              </p>
              <p>Map: {JSON.stringify(Array.from(currentStepData.map.entries()))}</p>
            </div>
          )}

          {currentStepData.type === "found" && (
            <div>
              <p>
                Found: nums[{currentStepData.index1}] = {currentStepData.value1} and nums[{currentStepData.index2}] = {currentStepData.value2}
              </p>
            </div>
          )}

          {currentStepData.type === "not_found" && (
            <div>
              <p>No solution found.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default TwoSumVisualizer;
