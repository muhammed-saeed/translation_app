import axios from "axios";

export const translateNote = async (note) => {
  console.log(note);
  const response = await axios.post(
    "/pcm_en",
    {
      title: note.title,
      details: note.details,
      cateogry: note.cateogry,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  if (response.status === 200) return response.data;
};


export const translateENtoPCM = async (note) => {
  console.log(note);
  const response = await axios.post(
    "/enpcm",
    {
      title: note.title,
      details: note.details,
      cateogry: note.cateogry,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  if (response.status === 200) return response.data;
};
export const discourse_classification = async (note) => {
  console.log(note);
  const response = await axios.post(
    "http://127.0.0.1:8080/api/parser",
    // "https://localhost:8080/discourseClassifier",
    {
      title: note.title,
      details: note.details,
      cateogry: note.cateogry,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  if (response.status === 200) return response.data;
};