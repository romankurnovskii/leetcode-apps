import React, { useState, useEffect, useMemo, useCallback } from "react";

const AddTwoNumbersVisualizer = () => {
  const [l1, setL1] = useState([2, 4, 3]);
  const [l2, setL2] = useState([5, 6, 4]);
  const [visualizationSteps, setVisualizationSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1);
  const [isDesktop, setIsDesktop] = useState(window.innerWidth >= 768);
  const [hover, setHover] = useState(false);

  // Linked List Node Component
  const ListNode = ({ value, isCurrent }) => (
    <div
      style={{
        border: "1px solid #e5e5e5",
        borderRadius: "50%",
        width: "30px",
        height: "30px",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: isCurrent ? "#007aff" : "white",
        color: isCurrent ? "white" : "black",
        margin: "0 5px",
      }}
    >
      {value}
    </div>
  );

  // Memoized generateVisualization function
  const generateVisualization = useMemo(() => {
    return (l1, l2) => {
      const steps = [];
      let carry = 0;
      let p = 0,
        q = 0;
      let sumList = [];

      steps.push({ type: "initial", l1: [...l1], l2: [...l2], carry: 0, sumList: [], message: "Initialize lists and carry." });

      while (p < l1.length || q < l2.length) {
        const x = p < l1.length ? l1[p] : 0;
        const y = q < l2.length ? l2[q] : 0;
        steps.push({
          type: "get_digits",
          p,
          q,
          x,
          y,
          carry,
          sumList: [...sumList],
          l1: [...l1],
          l2: [...l2],
          message: `Get digits l1[${p}] = ${x} and l2[${q}] = ${y}.`,
        });

        const sum = x + y + carry;
        steps.push({
          type: "calculate_sum",
          p,
          q,
          x,
          y,
          carry,
          sum,
          sumList: [...sumList],
          l1: [...l1],
          l2: [...l2],
          message: `Calculate sum = ${x} + ${y} + ${carry} = ${sum}.`,
        });

        carry = Math.floor(sum / 10);
        const digit = sum % 10;

        steps.push({
          type: "get_digit_and_carry",
          p,
          q,
          digit,
          carry,
          sumList: [...sumList],
          l1: [...l1],
          l2: [...l2],
          message: `Digit = ${sum} % 10 = ${digit}, Carry = ${Math.floor(sum / 10)}.`,
        });

        sumList.push(digit);
        steps.push({
          type: "add_to_sumlist",
          p,
          q,
          digit,
          carry,
          sumList: [...sumList],
          l1: [...l1],
          l2: [...l2],
          message: `Add digit ${digit} to sumList. sumList = ${JSON.stringify(sumList)}`,
        });

        p++;
        q++;
      }

      if (carry > 0) {
        steps.push({ type: "add_carry", carry, sumList: [...sumList], l1: [...l1], l2: [...l2], message: `Add carry ${carry} to sumList.` });
        sumList.push(carry);
      }

      steps.push({ type: "final", sumList: [...sumList], message: `Final sumList = ${JSON.stringify(sumList)}` });
      return steps;
    };
  }, []);

  useEffect(() => {
    setVisualizationSteps(generateVisualization(l1, l2));
    setCurrentStep(0);
  }, [l1, l2, generateVisualization]);

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
      <div style={{ display: isDesktop ? "flex" : "block", justifyContent: "space-between" }}>
        <div style={{ width: isDesktop ? "40%" : "100%", padding: "0.5rem" }}>
          <div style={{ marginBottom: "0.5rem" }}>
            <label htmlFor="l1" style={{ display: "block", fontSize: "0.875rem", marginBottom: "0.25rem" }}>
              List 1:
            </label>
            <input
              type="text"
              id="l1"
              style={{ width: "100%", padding: "0.5rem", borderRadius: "4px", border: "1px solid #e5e5e5" }}
              value={JSON.stringify(l1)}
              onChange={(e) => setL1(JSON.parse(e.target.value))}
            />
          </div>
          <div style={{ marginBottom: "0.5rem" }}>
            <label htmlFor="l2" style={{ display: "block", fontSize: "0.875rem", marginBottom: "0.25rem" }}>
              List 2:
            </label>
            <input
              type="text"
              id="l2"
              style={{ width: "100%", padding: "0.5rem", borderRadius: "4px", border: "1px solid #e5e5e5" }}
              value={JSON.stringify(l2)}
              onChange={(e) => setL2(JSON.parse(e.target.value))}
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
            onChange={(e) => handleSliderChange(e)}
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
              <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
                List 1:{" "}
                {l1.map((val, idx) => (
                  <ListNode key={idx} value={val} />
                ))}
              </div>
              <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
                List 2:{" "}
                {l2.map((val, idx) => (
                  <ListNode key={idx} value={val} />
                ))}
              </div>
            </div>
          )}

          {currentStepData.type === "get_digits" && (
            <div>
              <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
                List 1:{" "}
                {l1.map((val, idx) => (
                  <ListNode key={idx} value={val} isCurrent={idx === currentStepData.p} />
                ))}
              </div>
              <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
                List 2:{" "}
                {l2.map((val, idx) => (
                  <ListNode key={idx} value={val} isCurrent={idx === currentStepData.q} />
                ))}
              </div>
              <p>
                x = {currentStepData.x}, y = {currentStepData.y}, carry = {currentStepData.carry}
              </p>
            </div>
          )}

          {currentStepData.type === "calculate_sum" && (
            <div>
              <p>
                {currentStepData.x} + {currentStepData.y} + {currentStepData.carry} = {currentStepData.sum}
              </p>
            </div>
          )}

          {currentStepData.type === "get_digit_and_carry" && (
            <div>
              <p>
                Digit: {currentStepData.digit}, Carry: {currentStepData.carry}
              </p>
            </div>
          )}

          {currentStepData.type === "add_to_sumlist" && (
            <div>
              <p>Sum List: {JSON.stringify(currentStepData.sumList)}</p>
            </div>
          )}

          {currentStepData.type === "add_carry" && (
            <div>
              <p>Carry: {currentStepData.carry}</p>
            </div>
          )}

          {currentStepData.type === "final" && (
            <div>
              <p>Final Sum List: {JSON.stringify(currentStepData.sumList)}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AddTwoNumbersVisualizer;
