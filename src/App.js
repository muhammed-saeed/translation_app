import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Notes from "./pages/Notes";
import Create from "./pages/Create";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
import { purple } from "@material-ui/core/colors";
import Layout from "./components/Layout";
import { NoteFormProvider } from "./context/notes.context";
import {NoteFormProviderENPCM} from "./context/enpcm.context"
import { NoteFormProviderDiscourseClassifier } from "./context/discourse_classifier.context";
import { NoteFormProviderDiscourseClassifierEN } from "./context/discourse_classifierEN.context";
import CreateNote from "./pages/CreateNote";
import ENtoPCM from "./pages/ENtoPCM";
import DiscourseClassifier from"./pages/discourse_classifier"
import DiscourseClassifierEN from "./pages/discourse_classifierEN";


const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#fefefe",
    },
    secondary: purple,
  },
  typography: {
    fontFamily: "Quicksand",
    fontWeightLight: 400,
    fontWeightRegular: 500,
    fontWeightMedium: 600,
    fontWeightBold: 700,
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <Layout>
          <Switch>
            <Route exact path="/">
              <Notes />
            </Route>
            <Route path="/pcmen">
              <NoteFormProvider>
                <CreateNote />
              </NoteFormProvider>
            </Route>
            <Route path="/enpcm">
              <NoteFormProviderENPCM>
                <ENtoPCM />
              </NoteFormProviderENPCM>
            </Route>
            <Route path="/discourse_classifier">
              <NoteFormProviderDiscourseClassifier>
                <DiscourseClassifier />
              </NoteFormProviderDiscourseClassifier>
            </Route>

            <Route path="/discourse_classifier_en">
              <NoteFormProviderDiscourseClassifierEN>
                <DiscourseClassifierEN />
              </NoteFormProviderDiscourseClassifierEN>
            </Route>
          </Switch>
        </Layout>
      </Router>
    </ThemeProvider>
  );
}

export default App;
