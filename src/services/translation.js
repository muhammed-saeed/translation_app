import axios from "axios";

const backend_api="https://api.phrasetuner.com";

const instance = axios.create({
	  baseURL: backend_api,
});


export const translateNote = async (note) => {
  console.log(note);
  const response = await instance.post(
    `${backend_api}/pcm_en`,
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
  const response = await instance.post(
    `${backend_api}/enpcm`,
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



export const translateENtoAR = async (note) => {
  console.log(note);
  const response = await instance.post(
    `${backend_api}/en2ar`,
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
