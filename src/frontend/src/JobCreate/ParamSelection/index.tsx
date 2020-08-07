import React from "react";
import { Fade } from "@material-ui/core";
import { useStyles } from "../style";
import { Param, ParamValues } from "../../util/param";
import { Load, LoadFailedProps } from "../../Load";
import { ParamFields } from "../../ParamFields";

interface ParamSelectionProps {
    topicId: number;
    params: Param[] | undefined;
    values: ParamValues;
    loadFailedProps: LoadFailedProps;
    selectParamHandler: (key: string, value: any) => void;
}

export const ParamSelection: React.FC<ParamSelectionProps> = (props) => {
    const classes = useStyles();

    return (
        <Fade in={true}>
            <div className={classes.centerDivMedium}>
                <Load data={props.params} failed={props.loadFailedProps} className={classes.SPaddingTB}>
                    {props.params?.length !== 0
                        ?
                        <ParamFields
                            params={props.params}
                            values={props.values}
                            selectParamHandler={props.selectParamHandler}
                            disabled={false}
                            required={true}
                        />
                        :
                        <div className={classes.MPaddingTB} style={{ textAlign: "center" }}>
                            Für dieses Thema stehen keine Parameter zur Verfügung.
                        </div>}
                </Load>
            </div>
        </Fade>

    );
};