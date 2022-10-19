import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Notes from "./pages/Notes";
import Create from "./pages/Create";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
import { purple } from "@material-ui/core/colors";
import Layout from "./components/Layout";
import { NoteFormProvider } from "./context/notes.context";
import {NoteFormProviderENPCM} from "./context/enpcm.context"
import {NoteFormProviderENAR} from "./context/en2ar.context"
import {NoteFormProviderParaEN} from "./context/paraEN.context"
import CreateNote from "./pages/CreateNote";
import ENtoPCM from "./pages/ENtoPCM";
import En2AR from "./pages/EN2AR"
import ParaEN from "./pages/ParaEN";

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
            <Route path="/translation">
              <NoteFormProvider>
                <CreateNote />
              </NoteFormProvider>
            </Route>
            <Route path="/enpcm">
              <NoteFormProviderENPCM>
                <ENtoPCM />
              </NoteFormProviderENPCM>
            </Route>
            <Route path="/en2ar">
              <NoteFormProviderENAR>
                <En2AR />
              </NoteFormProviderENAR>
            </Route>

            <Route path="/paraEN">
              <NoteFormProviderParaEN>
                <ParaEN />
              </NoteFormProviderParaEN>
            </Route>
          </Switch>
        </Layout>
      </Router>
    </ThemeProvider>
  );
}

export default App;
