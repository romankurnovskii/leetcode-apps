import React, {useState, useEffect, useMemo, useCallback} from "react";

const ContainerWithMostWaterVisualizer = () => {
  const [heights, setHeights] = useState([1, 8, 6, 2, 5, 4, 8, 3, 7]);
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hover, setHover] = useState(false);

  const generateVisualization = useMemo(() => {
    return (heights) => {
      const steps = [];
      let left = 0;
      let right = heights.length - 1;
      let maxArea = 0;

      steps.push({type: "initial", heights: [...heights], left, right, maxArea, message: "Initialize pointers and maxArea."});

      while (left < right) {
        const area = Math.min(heights[left], heights[right]) * (right - left);
        steps.push({
          type: "calculate_area",
          heights: [...heights],
          left,
          right,
          area,
          maxArea,
          message: `Calculate area with left=${left}, right=${right}. Area = ${Math.min(heights[left], heights[right])} * ${right - left} = ${area}`,
        });

        if (area > maxArea) {
          maxArea = area;
          steps.push({type: "update_max_area", heights: [...heights], left, right, area, maxArea, message: `Update maxArea to ${maxArea}.`});
        }

        if (heights[left] < heights[right]) {
          left++;
          steps.push({type: "move_left", heights: [...heights], left, right, maxArea, message: `Move left pointer to ${left}.`});
        } else {
          right--;
          steps.push({type: "move_right", heights: [...heights], left, right, maxArea, message: `Move right pointer to ${right}.`});
        }
      }

      steps.push({type: "final", maxArea, message: `Final maxArea = ${maxArea}.`});
      return steps;
    };
  }, []);

  useEffect(() => {
    setVisualizationSteps(generateVisualization(heights));
    setCurrentStep(0);
  }, [heights, generateVisualization]);

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
    let intervalId;
    if (isPlaying) {
      intervalId = setInterval(() => {
        setCurrentStep((prevStep) => (prevStep < visualizationSteps.length - 1 ? prevStep + 1 : 0));
      }, 1000 / speed);
    } else {
      clearInterval(intervalId);
    }
    return () => clearInterval(intervalId);
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

  const PlayIcon = () => (
    <svg viewBox="0 0 24 24" style={{height: "1.2rem", width: "1.2rem"}}>
      <path fill="currentColor" d="M6 4l12 8L6 20V4z" />
    </svg>
  );

  const PauseIcon = () => (
    <svg viewBox="0 0 24 24" style={{height: "1.2rem", width: "1.2rem"}}>
      <path fill="currentColor" d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" />
    </svg>
  );

  const BackIcon = () => (
    <svg viewBox="0 0 24 24" style={{height: "1.2rem", width: "1.2rem"}}>
      <path fill="currentColor" d="M11.67 3.87L9.9 2.1 0 12l9.9 9.9 1.77-1.77L3.54 12z" />
    </svg>
  );

  const ForwardIcon = () => (
    <svg viewBox="0 0 24 24" style={{height: "1.2rem", width: "1.2rem"}}>
      <path fill="currentColor" d="M12.33 3.87L14.1 2.1 24 12l-9.9 9.9-1.77-1.77L20.46 12z" />
    </svg>
  );

  const ResetIcon = () => (
    <svg viewBox="0 0 24 24" style={{height: "1.2rem", width: "1.2rem"}}>
      <path
        fill="currentColor"
        d="M13 3c-4.97 0-9 4.03-9 9H3l4 5 4-5H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06L9.29 16.29C10.86 17.86 12.85 18.67 15 18.67c4.97 0 9-4.03 9-9s-4.03-9-9-9z"
      />
    </svg>
  );

  const handleSliderChange = (event) => {
    setCurrentStep(parseInt(event.target.value, 10));
    setIsPlaying(false);
  };

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
      <div style={{display: isDesktop ? "flex" : "block", justifyContent: "space-between"}}>
        <div style={{width: isDesktop ? "40%" : "100%", padding: "0.5rem"}}>
          <div style={{marginBottom: "0.5rem"}}>
            <label htmlFor="heights" style={{display: "block", fontSize: "0.875rem", marginBottom: "0.25rem"}}>
              Heights:
            </label>
            <input
              type="text"
              id="heights"
              style={{width: "100%", padding: "0.5rem", borderRadius: "4px", border: "1px solid #e5e5e5"}}
              value={JSON.stringify(heights)}
              onChange={(e) => setHeights(JSON.parse(e.target.value))}
            />
          </div>

          <div style={{display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "0.5rem"}}>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px"}}
              onClick={handlePrevious}
              disabled={currentStep === 0}
            >
              <BackIcon />
            </button>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px"}}
              onClick={handlePlayPause}
            >
              {isPlaying ? <PauseIcon /> : <PlayIcon />}
            </button>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px"}}
              onClick={handleNext}
              disabled={currentStep === visualizationSteps.length - 1}
            >
              <ForwardIcon />
            </button>
            <button
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{backgroundColor: "transparent", border: "none", cursor: "pointer", padding: "0.25rem", borderRadius: "4px"}}
              onClick={handleReset}
            >
              <ResetIcon />
            </button>
          </div>
          <div style={{display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "0.5rem"}}>
            <label htmlFor="animationSpeed" style={{fontSize: "0.75rem"}}>
              Animation Speed:
            </label>
            <input
              type="number"
              id="animationSpeed"
              style={{width: "60px", padding: "0.25rem", borderRadius: "4px", border: "1px solid #e5e5e5", fontSize: "0.75rem"}}
              value={speed}
              onChange={(e) => setSpeed(parseInt(e.target.value))}
            />
          </div>
          <div style={{display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "0.5rem"}}>
            <span style={{fontSize: "0.75rem"}}>
              Step {currentStep + 1} of {totalSteps}
            </span>
          </div>
          <input type="range" min="0" max={visualizationSteps.length - 1} value={currentStep} onChange={handleSliderChange} style={{width: "100%"}} />
        </div>
        <div style={{width: isDesktop ? "60%" : "100%", padding: "0.5rem", borderLeft: isDesktop ? "1px solid #e5e5e5" : "none"}}>
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
              <p>Heights: {JSON.stringify(currentStepData.heights)}</p>
            </div>
          )}

          {currentStepData.type === "calculate_area" && (
            <div>
              <p>
                Left: {currentStepData.left}, Right: {currentStepData.right}
              </p>
              <p>Area: {currentStepData.area}</p>
            </div>
          )}

          {currentStepData.type === "update_max_area" && (
            <div>
              <p>Max Area: {currentStepData.maxArea}</p>
            </div>
          )}

          {currentStepData.type === "move_left" && (
            <div>
              <p>Moving Left to: {currentStepData.left}</p>
            </div>
          )}

          {currentStepData.type === "move_right" && (
            <div>
              <p>Moving Right to: {currentStepData.right}</p>
            </div>
          )}

          {currentStepData.type === "final" && (
            <div>
              <p>Final Max Area: {currentStepData.maxArea}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ContainerWithMostWaterVisualizer;
