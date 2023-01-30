import axios from "axios";
// require('dotenv').config()

export const translateNote = async (note) => {
  console.log(note);
  const response = await axios.post(
    `${process.env.REACT_APP_API_2}/pcm_en`,
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
    `${process.env.REACT_APP_API_2}/enpcm`,
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
    // "/api/parser",
    `${process.env.REACT_APP_API_1}/api/parseren/`,
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


export const discourse_classificationEN = async (note) => {
  console.log(note);
  const response = await axios.post(
    // "/api/parser",
    `${process.env.REACT_APP_API_1}/api/parseren/`,
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
