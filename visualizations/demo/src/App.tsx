import React, {useState} from "react";
import RemoteComponentViewer, {InputCase, NextButton, PreviousButton, StartButton} from "leetcode-apps-components";

function App() {
  const [input, setInput] = useState("");
  const [step, setStep] = useState(0);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 p-4 gap-8">
      <div className="max-w-md w-full bg-white rounded-xl shadow-lg p-8 space-y-6">
        <div>
          <h2 className="text-2xl font-bold mb-1">Reusable Components Demo</h2>
          <p className="text-gray-500 mb-4">Try the input and stepper buttons below. Each button uses a distinct color for best UX.</p>
        </div>
        <InputCase
          label="Your Input"
          value={input}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => setInput(e.target.value)}
          placeholder="Type something..."
        />
        <div className="flex flex-col gap-2">
          <span className="text-sm text-gray-600">Stepper Controls:</span>

          <div className="flex gap-3 rounded-lg p-3 justify-center border border-gray-200">
            <StartButton onClick={() => setStep(0)} disabled={step === 0} />
            <PreviousButton onClick={() => setStep((s) => Math.max(0, s - 1))} disabled={step === 0} />
            <NextButton onClick={() => setStep((s) => s + 1)} />
          </div>
        </div>
        <div className="text-center mt-2">
          <span className="inline-block px-3 py-1 rounded-full bg-blue-100 text-blue-700 font-semibold">Current step: {step}</span>
        </div>
      </div>

      <div className="max-w-md w-full bg-white rounded-xl shadow-lg p-8 space-y-6">
        Raw Import
        <RemoteComponentViewer problemId={1768} />
      </div>
    </div>
  );
}

export default App;
