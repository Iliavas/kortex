import react from "react";
import { Button, ButtonTypes } from "../../Button/Button";
import { Input } from "../../Input/Input";
import { Text } from "../../Text/Text";
import { Textarea } from "../../Textarea/Textarea";
import { BasePopUp } from "../BasePopUp/BasePopUp";

import "./style.css";

interface ICreateBlock{
    onCreate:(descr:string, name:string, subHead:string) => void;
    onDelete:Function;
}

export const CreateBlockPopUp:react.FC<ICreateBlock> = (props) => {

    var descr = "";
    var name = "";

    var subHead = "";

    return <BasePopUp deleteFunc={props.onDelete}>
        <Text className="create-block__text">Создать блок</Text>
        <Input onChange={(e:string) => {name = e}} placeholder={"Название"}></Input>
        <Input onChange={(e:string) => {subHead=e}} placeholder="Подзаголовок"></Input>
        <Textarea onChange={(e:string) => {descr = e}}></Textarea>
        <Button type={ButtonTypes.red} onClick={() => {
            console.log(descr, name)
            props.onCreate(descr, name, subHead)
        }}>Создать</Button>
    </BasePopUp>
}