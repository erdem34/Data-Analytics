from visuanalytics.analytics.control.jobs.job import Job
from visuanalytics.analytics.control.steps.weather import WeatherSteps

# TODO(Max) Implement (current just for testing)

Job("1", WeatherSteps("Config")).start()
