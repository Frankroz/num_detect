import DigitCanvas from "./components/DigitCanvas";

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-slate-900 via-slate-950 to-black">
      <div className="max-w-xl w-full text-center space-y-4 mb-12">
        <h1 className="text-6xl font-black tracking-tight text-white italic underline decoration-blue-500">
          Detect your number
        </h1>
        <p className="text-slate-400 text-lg">
          Draw a single digit in the box below and watch the neural network
          classify it in real-time. Using MNIST.AI
        </p>
      </div>

      <main className="w-full max-w-lg">
        <DigitCanvas />
      </main>

      <footer className="mt-20 text-slate-500 text-xs font-mono">
        FASTAPI BACKEND • TENSORFLOW MODEL • REACT VITE FRONTEND
        <p className="mt-10 text-slate-400 text-xs font-mono">
          Created by Francisco R
        </p>
      </footer>
    </div>
  );
}

export default App;
