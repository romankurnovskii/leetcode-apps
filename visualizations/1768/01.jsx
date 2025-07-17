import React, {useState, useEffect} from "react";
import {InputCase, NextButton, PreviousButton, StartButton} from "leetcode-apps-components";

// Component to display the current step information
const StepInfo = ({stepNumber, totalSteps, description, titleClassName, descriptionClassName}) => (
  <div className="p-6 rounded-xl border">
    <h2 className={titleClassName}>
      Current Step: {stepNumber} / {totalSteps}
    </h2>
    <p className={descriptionClassName}>{description}</p>
  </div>
);

// Component to display a sequence of characters with optional highlighting
const CharacterSequence = ({label, characters, highlightIndex, containerClassName, charClassName, highlightCharClassName}) => (
  <div className={containerClassName}>
    {label && <div className="mb-2">{label}:</div>}
    <div className="flex flex-wrap justify-center text-2xl font-mono min-h-[40px]">
      {characters.map((char, idx) => (
        <span
          key={`${label}-${idx}-${char}`}
          className={`${charClassName} ${
            highlightIndex === idx || (Array.isArray(highlightIndex) && highlightIndex.includes(idx)) ? highlightCharClassName : ""
          }`}
        >
          {char}
        </span>
      ))}
    </div>
  </div>
);

// --- Standalone Merge Alternately Visualizer Component ---
function App() {
  const [word1, setWord1] = useState("abc");
  const [word2, setWord2] = useState("pqr");
  const [mergedResult, setMergedResult] = useState("");

  const [steps, setSteps] = useState([]);
  const [currentStepIndex, setCurrentStepIndex] = useState(-1);

  // Logic
  const handlerStart = (w1, w2) => {
    let res = [];
    let currentSteps = [];
    let i = 0;

    // Initial state
    currentSteps.push({
      description: `Starting merge with "${w1}" and "${w2}".`,
      res: [],
      highlight1: -1,
      highlight2: -1,
      currentWord1: w1,
      currentWord2: w2,
      pointerI: i,
    });

    // Loop while both words have characters
    while (i < w1.length && i < w2.length) {
      // Step 1: Append character from word1
      res.push(w1[i]);
      currentSteps.push({
        description: `Step ${currentSteps.length}: Appending '${w1[i]}' from word1.`,
        res: [...res], // Create a copy to ensure immutability for state updates
        highlight1: i,
        highlight2: -1,
        currentWord1: w1,
        currentWord2: w2,
        pointerI: i,
      });

      // Step 2: Append character from word2
      res.push(w2[i]);
      currentSteps.push({
        description: `Step ${currentSteps.length}: Appending '${w2[i]}' from word2.`,
        res: [...res],
        highlight1: -1,
        highlight2: i,
        currentWord1: w1,
        currentWord2: w2,
        pointerI: i,
      });
      i++;
    }

    // After loop, append remaining characters from word1 (if any)
    if (i < w1.length) {
      const remainingWord1 = w1.substring(i);
      res.push(remainingWord1);
      currentSteps.push({
        description: `Step ${currentSteps.length}: Appending remaining characters from word1: "${remainingWord1}".`,
        res: [...res],
        highlight1: Array.from({length: w1.length - i}, (_, k) => k + i), // Highlight all remaining chars
        highlight2: -1,
        currentWord1: w1,
        currentWord2: w2,
        pointerI: i,
      });
    }

    // After loop, append remaining characters from word2 (if any)
    if (i < w2.length) {
      const remainingWord2 = w2.substring(i);
      res.push(remainingWord2);
      currentSteps.push({
        description: `Step ${currentSteps.length}: Appending remaining characters from word2: "${remainingWord2}".`,
        res: [...res],
        highlight1: -1,
        highlight2: Array.from({length: w2.length - i}, (_, k) => k + i), // Highlight all remaining chars
        currentWord1: w1,
        currentWord2: w2,
        pointerI: i,
      });
    }

    const finalResult = res.join("");
    currentSteps.push({
      description: `Final result: Joining all parts to get "${finalResult}".`,
      res: [...res],
      highlight1: -1,
      highlight2: -1,
      currentWord1: w1,
      currentWord2: w2,
      pointerI: i,
    });

    setSteps(currentSteps);
    setMergedResult(finalResult);
    setCurrentStepIndex(0); // Start from the first step
  };

  const handlerPrevStep = () => {
    setCurrentStepIndex((prevIndex) => Math.max(prevIndex - 1, 0));
  };

  const handlerNextStep = () => {
    setCurrentStepIndex((prevIndex) => Math.min(prevIndex + 1, steps.length - 1));
  };

  // Effect to run the merge when component mounts or words change
  useEffect(() => {
    handlerStart(word1, word2);
  }, [word1, word2]);

  const currentStep = steps[currentStepIndex];

  return (
    <div>
      {/* Input Section */}
      <div className="flex flex-col md:flex-row gap-2">
        <InputCase label="Word 1" value={word1} onChange={(e) => setWord1(e.target.value)} placeholder="Enter first word" />
        <InputCase label="Word 2" value={word2} onChange={(e) => setWord2(e.target.value)} placeholder="Enter second word" />
      </div>

      {/* Action Buttons */}
      <div className="flex justify-center gap-2">
        <StartButton onClick={() => handlerStart(word1, word2)} />
        <PreviousButton onClick={handlerPrevStep} disabled={currentStepIndex <= 0} />
        <NextButton onClick={handlerNextStep} disabled={currentStepIndex >= steps.length - 1} />
      </div>

      {/* Visualization Area */}
      {currentStep && (
        <div className="p-6 rounded-xl border">
          <StepInfo
            stepNumber={currentStepIndex + 1}
            totalSteps={steps.length}
            description={currentStep.description}
            titleClassName="text-xl font-semibold mb-4"
            descriptionClassName="text-lg mb-4"
          />

          <div className="flex flex-col items-center mb-4">
            <CharacterSequence
              label="Word 1"
              characters={currentStep.currentWord1.split("")}
              highlightIndex={currentStep.highlight1}
              containerClassName="mb-4"
              charClassName="p-2 mx-0.5 rounded-md transition-colors duration-300"
              highlightCharClassName="font-bold scale-110"
            />

            <CharacterSequence
              label="Word 2"
              characters={currentStep.currentWord2.split("")}
              highlightIndex={currentStep.highlight2}
              containerClassName="mb-4"
              charClassName="p-2 mx-0.5 rounded-md transition-colors duration-300"
              highlightCharClassName="font-bold scale-110"
            />

            <CharacterSequence
              label="Current Merged Result (res array)"
              characters={currentStep.res}
              containerClassName="mb-4"
              charClassName="p-2 mx-0.5 my-0.5 rounded-md"
              highlightCharClassName=""
            />
          </div>

          <div className="text-xl font-bold mt-6 text-center">
            Final Merged String: <span className="">{mergedResult}</span>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
