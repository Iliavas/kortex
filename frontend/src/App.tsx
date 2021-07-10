import react, { useState } from "react";

import {Provider} from "react-redux";

import {
    BrowserRouter as Router,
    Route,
    Switch,
    Redirect
} from "react-router-dom";
import { ScreenWithCheckboxes } from "./screens/ScreenWithCheckboxes/ScreenWidthCheckboxes";
import { ViewCard } from "./screens/ViewCard/ViewCard";
import {useGetStateQuery} from "./generated/graphql";
import { Registration } from "./screens/Registration/Registration";
import { Login } from "./screens/Login/Login";
import { GlobalHeader } from "./uikit/GlobalHeader/GlobalHeader";

import {ViewCardEdit} from "./screens/ViewCard/ViewCardEdit";

import store from "./store/store";

import "./App.css";

export enum Theme{
    Light,
    Dark
}

export const ThemeContext = react.createContext({
    theme: Theme.Dark,
    setTheme: (a:any) => {},
    setSwitcherVisibility: (visible:boolean) => {}
})

export const App:react.FC = () => {

    const {data, loading} = useGetStateQuery({
        variables:{token:localStorage.getItem("token")},
        onCompleted:(e) => {
            //setTheme(
            //    e.getVisitByUser?.theme == "Light" ? Theme.Light : Theme.Dark
            //)
        }
    })

    const [theme, setTheme] = react.useState(Theme.Light);

    const [visibility, setVisibility] = useState(true);

    if (theme == Theme.Dark) {
        let root = document.body;
        root.style.setProperty("--back-color", "linear-gradient(174.96deg, #252A2E 0%, #15191D 95.95%)");
    }
    else{
        let root = document.body;
        root.style.setProperty("--back-color", "#fff");
    }

    if (loading) {
        return <div></div>
    }


    return <Provider store={store}>
            <ThemeContext.Provider value={{
        theme:theme, setTheme:setTheme,
        setSwitcherVisibility: setVisibility
        }}>
            
        <Router>
            <GlobalHeader></GlobalHeader>   
            <div className="centered">
                <div className="global-container">
                    <Switch>
                    <Route path={"/registration"}>
                        <Registration></Registration>
                    </Route>
                    <Route path="/login">
                        <Login></Login>
                    </Route>
                    <Route path="/index">
                        <ScreenWithCheckboxes></ScreenWithCheckboxes>
                    </Route>
                    <Route path="/set">
                        <ScreenWithCheckboxes></ScreenWithCheckboxes>
                    </Route>
                    <Route path="/:id/view">
                        <ViewCardEdit></ViewCardEdit>
                    </Route>
                    <Route path="/:id">
                        <ViewCard></ViewCard>
                    </Route>
                    <Route path="">
                        <Redirect to={"index"}></Redirect>
                    </Route>
                </Switch>
                </div>
            </div>
            
        </Router>
    </ThemeContext.Provider>

    </Provider> 
}
