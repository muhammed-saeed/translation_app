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
import useNoteForm from "../context/discourse_classifierEN.context";

const useStyles = makeStyles({
  field: {
    marginTop: 20,
    marginBottom: 20,
    display: "block",
  },
});

const DiscourseClassifierEN = () => {
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
        Please enter EN to be parsed
      </Typography>

      <form noValidate autoComplete="off" onSubmit={handleSubmit}>
      <TextField
          className={classes.field}
          onChange={(e) => noteFormChanged("details", e.target.value)}
          label="Enter EN text please"
          variant="outlined"
          color="secondary"
          multiline
          rows={6}
          fullWidth
          required
          value={note.details}
          error={detailsError}
        />

        <TextField
          className={classes.field}
          onChange={(e) => noteFormChanged("title", e.target.value)}
          label="Relations output will be here "
          variant="outlined"
          color="secondary"
          fullWidth
          multiline
          rows={8}
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
            Extract the relations
          </Button>
        )}
      </form>
    </Container>
  );
};

export default DiscourseClassifierEN;
