import React, { useState, useCallback } from "react";
import { Param, ParamValues } from "../util/param";
import { JobItem } from "./JobItem";
import {Fade, Grid, Paper, Typography} from "@material-ui/core";
import { useFetchMultiple } from "../Hooks/useFetchMultiple";
import { Load } from "../Load";
import { Schedule } from "../util/schedule";
import { getUrl } from "../util/fetchUtils";
import {useStyles} from "../Home/style";
import {ContinueButton} from "../JobCreate/ContinueButton";
import InfoOutlinedIcon from '@material-ui/icons/InfoOutlined';
import {ComponentContext} from "../ComponentProvider";

export interface Job {
  jobId: number;
  jobName: string;
  params: Param[];
  values: ParamValues;
  schedule: Schedule;
  topicId: number;
  topicName: string;
}

export const JobList: React.FC = () => {
  const classes = useStyles();
  const components = React.useContext(ComponentContext);

  const [loadFailed, setLoadFailed] = useState(false);
  const handleLoadFailed = useCallback(() => {
    setLoadFailed(true);
  }, [setLoadFailed]);

  const [jobInfo, getJobs] = useFetchMultiple<Job[]>(
    getUrl("/jobs"),
    undefined,
    handleLoadFailed
  );

  const handleReaload = () => {
    setLoadFailed(false);
    getJobs();
  };

  if (jobInfo?.length === 0) {
      return (
          <Fade in={true}>
              <Paper variant="outlined" className={classes.paper}>
                  <Grid container spacing={2}>
                      <Grid container item justify="center">
                          <InfoOutlinedIcon
                              className={classes.infoIcon}
                              color={"disabled"}
                              fontSize={"default"}
                          />
                      </Grid>
                      <Grid container item justify="center">
                          <Typography gutterBottom variant={"h5"}>
                              Willkommen bei ihrer Job Übersicht!
                          </Typography>
                          <Typography align={"center"} color="textSecondary">
                              Mit VisuAnalytics können Sie sich Videos zu bestimmten Themen generieren lassen.<br/> Klicken Sie auf 'Neuen Job erstellen', um Ihren ersten Job anzulegen und ein Video zu einem gewählten Zeitraum generieren zu lassen.
                          </Typography>
                      </Grid>
                      <Grid container item justify="center">
                          <ContinueButton style={{width: "auto"}} onClick={() => components?.setCurrent("jobPage")}>Neuen Job erstellen</ContinueButton>
                      </Grid>
                  </Grid>
              </Paper>
          </Fade>
      )
  } else {
      return (
          <Fade in={true}>
              <div>
                  <Load
                    failed={{
                      hasFailed: loadFailed,
                      name: "Jobs",
                      onReload: handleReaload,
                    }}
                    data={jobInfo}
                  >
                    {jobInfo?.map((j: Job) => (
                      <div key={j.jobId}>
                        <JobItem job={j} getJobs={handleReaload} />
                      </div>
                    ))}
                  </Load>
              </div>
          </Fade>
      )
  }
}