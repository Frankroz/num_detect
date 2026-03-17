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
        <a
          href={"https://github.com/Frankroz/num_detect"}
          className="flex p-6 justify-center item-center text-zinc-500 hover:text-[#00f2ff] transition-colors"
          target="_blank"
          rel="noopener noreferrer"
        >
          <span className="m-1">Source code</span>
          <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
          </svg>
        </a>
      </footer>
    </div>
  );
}

export default App;
