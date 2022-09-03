import React, { useState } from "react";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Container from "@material-ui/core/Container";
import KeyboardArrowRightIcon from "@material-ui/icons/KeyboardArrowRight";
import { CircularProgress, makeStyles } from "@material-ui/core";
import TextField from "@material-ui/core/TextField";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import { useHistory } from "react-router-dom";
import useNoteForm from "../context/notes.context";

const useStyles = makeStyles({
  field: {
    marginTop: 20,
    marginBottom: 20,
    display: "block",
  },
});

const CreateNote = () => {
  const classes = useStyles();
  const history = useHistory();
  const {
    note,
    noteFormChanged,
    handleSubmit,
    titleError,
    detailsError,
    submitting,
  } = useNoteForm();

  return (
    <Container size="sm">
      <Typography
        variant="h6"
        color="textSecondary"
        component="h2"
        gutterBottom
      >
        Please Enter PCM text to be translated into English
      </Typography>

      <form noValidate autoComplete="off" onSubmit={handleSubmit}>
      <TextField
          className={classes.field}
          onChange={(e) => noteFormChanged("details", e.target.value)}
          label="PCM To enlgish details"
          variant="outlined"
          color="secondary"
          multiline
          rows={4}
          fullWidth
          required
          value={note.details}
          error={detailsError}
        />

        <TextField
          className={classes.field}
          onChange={(e) => noteFormChanged("title", e.target.value)}
          label="Translated Text "
          variant="outlined"
          color="secondary"
          fullWidth
          
          value={note.title}
         
        />
       
        {/* <Radio value="hello" />
        <Radio value="goodbye" /> */}

        {/* <FormControl className={classes.field}>
          <FormLabel>Note Category</FormLabel>
          <RadioGroup
            value={note.category}
            onChange={(e) => noteFormChanged("category", e.target.value)}
          >
            <FormControlLabel value="money" control={<Radio />} label="Ernie" />
            <FormControlLabel value="todos" control={<Radio />} label="Merel" />
            <FormControlLabel
              value="reminders"
              control={<Radio />}
              label="PinJie"
            />
            <FormControlLabel
              value="work"
              control={<Radio />}
              label="Muhammed"
            />
          </RadioGroup>
        </FormControl> */}

        {submitting ? (
          <CircularProgress color="secondary" />
        ) : (
          <Button
            type="submit"
            color="secondary"
            variant="contained"
            endIcon={<KeyboardArrowRightIcon />}
          >
            Translate PCM to EN
          </Button>
        )}
      </form>
    </Container>
  );
};

export default CreateNote;
