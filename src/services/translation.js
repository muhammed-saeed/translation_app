import axios from "axios";

export const translateNote = async (note) => {
  console.log(note);
  const response = await axios.post(
    "/",
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
