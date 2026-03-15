import React, { useRef, useState } from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
import { Eraser, BrainCircuit, RefreshCw } from "lucide-react";
import { predictDigit } from "../services/api";

const DigitCanvas = () => {
  const canvasRef = useRef(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    try {
      const image = await canvasRef.current.exportImage("png");
      const result = await predictDigit(image);
      setPrediction(result.prediction);
    } catch (err) {
      console.error("Prediction failed", err);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    canvasRef.current.clearCanvas();
    setPrediction(null);
  };

  return (
    <div className="flex flex-col items-center gap-8">
      <div className="relative group">
        <div className="absolute -inset-1 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-2xl blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
        <div className="relative bg-white rounded-xl overflow-hidden shadow-2xl border-4 border-slate-800">
          <ReactSketchCanvas
            ref={canvasRef}
            strokeWidth={18}
            strokeColor="black"
            canvasColor="white"
            width="320px"
            height="320px"
          />
        </div>
      </div>

      <div className="flex gap-4">
        <button
          onClick={handleClear}
          className="flex items-center gap-2 px-6 py-3 text-white rounded-xl bg-slate-800 hover:bg-slate-700 transition-all font-semibold border border-slate-700"
        >
          <Eraser size={20} /> Clear
        </button>
        <button
          onClick={handlePredict}
          disabled={loading}
          className="flex items-center gap-2 px-8 py-3 text-white rounded-xl bg-blue-600 hover:bg-blue-500 transition-all font-bold shadow-lg shadow-blue-500/20 disabled:opacity-50"
        >
          {loading ? (
            <RefreshCw className="animate-spin" />
          ) : (
            <BrainCircuit size={20} />
          )}
          {loading ? "Analyzing..." : "Identify"}
        </button>
      </div>

      {prediction !== null && (
        <div className="text-center animate-in fade-in zoom-in duration-300">
          <p className="text-slate-400 text-sm font-mono tracking-tighter uppercase">
            Result
          </p>
          <h2 className="text-8xl font-black text-transparent bg-clip-text bg-gradient-to-b from-white to-blue-400">
            {prediction}
          </h2>
        </div>
      )}
    </div>
  );
};

export default DigitCanvas;
