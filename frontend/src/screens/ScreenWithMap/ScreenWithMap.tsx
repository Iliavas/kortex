import react from "react";
import { Route, Switch } from "react-router-dom";
import MapboxMap from "../../uikit/Map/Map";
import { Sidebar } from "../../uikit/Sidebar/Sidebar";
import { DetailsScreen } from "../DetailScreen/DetailScreen";
import { ListOfObjects } from "../ListOfObjects/ListOfObjects";
import { ProfileScreen } from "../ProfileScreen/ProfileScreen";
import { VideoUploadScreen } from "../VideoUploadScreen/VideoUploadScreen";

import "./style.css";

export const ScreenWithMap:react.FC = () => {
    return <div className="screen-with-map__container">
        <Sidebar></Sidebar>
        <Switch>
            <Route path="/index/:id/details">
                <DetailsScreen></DetailsScreen>
            </Route>
            <Route path="/index/video-upload">
                <VideoUploadScreen></VideoUploadScreen>
            </Route>
            <Route path="/index/object-list">
                <ListOfObjects></ListOfObjects>
            </Route>
            <Route path="/index/favorites">
                <ListOfObjects></ListOfObjects>
            </Route>
            <Route path="/index/viewed">
                <ListOfObjects></ListOfObjects>
            </Route>
            <Route path="/index/profile">
                <ProfileScreen></ProfileScreen>    
            </Route>
            <Route path="">
                <MapboxMap></MapboxMap>
            </Route>
            
        </Switch>
        
    </div>
}