import React, { createContext, useContext, useMemo, useState } from "react";
import { translateNote } from "../services/translation";
import {discourse_classification} from  "../services/translation"
const NoteFormContext = createContext({});

export const NoteFormProviderDiscourseClassifier = ({ children }) => {
  const [note, setNote] = useState({
    title: "wait the parse output will appear here",
    details: "",
    category: "money",
  });
  const [submitting, setSubmitting] = useState(false);
  const [titleError, setTitleError] = useState(false);
  const [detailsError, setDetailsError] = useState(false);

  const noteFormChanged = (name, value) => {
    setNote((prevState) => {
      return {
        ...prevState,
        [name]: value,
      };
    });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setTitleError(false);
    setDetailsError(false);
    console.log("Are you here");
    if (note.title == "") {
      setTitleError(true);
    }
    if (note.details == "") {
      setDetailsError(true);
    }
    if (note.title && note.details) {
      setSubmitting(true);
      const result = await discourse_classification(note);
      if (result) {
        setSubmitting(false);
        setNote((prevState) => {
          return {
            ...prevState,
            title: result.translatedDetails,
          };
        });
      }
    }
  };

  const memoedValue = useMemo(
    () => ({
      note,
      titleError,
      detailsError,
      noteFormChanged,
      handleSubmit,
      submitting,
    }),
    [note, submitting]
  );
  return (
    <NoteFormContext.Provider value={memoedValue}>
      {children}
    </NoteFormContext.Provider>
  );
};

export default function useNoteForm() {
  return useContext(NoteFormContext);
}
