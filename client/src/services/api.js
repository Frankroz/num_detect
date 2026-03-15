const BASE_URL = import.meta.env.VITE_BACKEND_URL

export const predictDigit = async (base64Image) => {
  try {
    const response = await fetch(`${BASE_URL}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // FastAPI expects a JSON object with a 'data' key based on our previous backend code
      body: JSON.stringify({ data: base64Image }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    return await response.json();
  } catch (error) {
    console.error("Error predicting digit:", error);
    return { error: "Failed to connect to backend" };
  }
};
