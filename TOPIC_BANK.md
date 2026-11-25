# Topic Bank

# Software Engineering Project Proposals

Eight project proposals for the Software Engineering class. Each one names the problem it solves, the algorithm it uses, the data it needs, and how it will be tested.

## How to Read This Document

Every proposal uses the same structure: problem, solution, algorithm, data, core features, software engineering deliverables, evaluation, risks, and difficulty.

Difficulty is rated for a team of about 3 to 4 students working for one term:

- **Moderate**: doable with steady effort.
- **Moderate-High**: ambitious, but doable if the scope stays controlled.

Proposal 7 builds directly on KampusKonek, the student council event, task, and approval platform from the WEBPROG project.

🔴 marks proposals the team will not consider (Proposals 4 and 5).

## Comparison at a Glance

| # | Proposal | Core algorithm | Data source | Difficulty |
|---|----------|----------------|-------------|------------|
| 1 | Event Attendance and Stay-Duration Predictor | Gradient boosting with survival-style labeling | Self-collected QR logs | Moderate |
| 2 | Diacritical Mapping for Text-to-Speech | Character-level BiLSTM with dictionary fallback | Public text corpus | Moderate-High |
| 3 | Pocket Almanac for Plants and Animals | MobileNet transfer learning (on-device) | iNaturalist, PlantVillage | Moderate-High |
| 🔴 4 | 🔴 Fire Risk Mapper from Aerial Imagery (not considered) | CNN or segmentation plus risk scoring | Open imagery and open map data | Moderate-High |
| 🔴 5 | 🔴 Habit and Addiction Risk Self-Monitor (not considered) | Logistic regression and gradient boosting on behavior logs | Self-reported or synthetic data | Moderate |
| 6 | Laguna Tourism Itinerary Planner | Orienteering-style route optimization plus recommender | Self-collected place data | Moderate |
| 7 | KampusKonek Task Risk Predictor | Gradient boosting for overdue risk, plus assignment-based workload balancing | KampusKonek task logs plus simulated council data | Moderate |
| 8 | Campus Queue Wait-Time Predictor | Time-series regression plus queueing estimates | Self-collected counts | Moderate |

---

## Proposal 1: Event Attendance and Stay-Duration Predictor

**Problem.** Paper sign-in sheets only prove that someone arrived. Organizers cannot tell who is about to leave early, so they cannot step in while the event is still running.

**Solution.** A web app that records participants by QR scan at checkpoints and predicts, for each participant, whether they will stay for the whole event. Organizers see a live dashboard of attendees who are likely to leave.

**Algorithm.** Gradient boosting (XGBoost or LightGBM) on features such as check-in delay, checkpoints completed, past attendance rate, and event type. For a second output, add a survival-style estimate of how much longer a person is likely to stay. Handle class imbalance with class weights and report calibrated probabilities.

**Data.** QR scan logs from at least two or three events, plus simulated events to add volume for testing. All identifiers are anonymized.

**Core features.**

- QR check-in and checkpoint scanning (mobile web)
- Organizer dashboard with a live at-risk list and an adjustable threshold
- Event creation, roster import, and post-event report export
- Model retraining script and versioned model file

**SE deliverables.** Requirements and use cases, REST API design, database schema, sequence diagram of the scan-to-prediction flow, unit and integration tests, and a load test with many scans at once.

**Evaluation.** F1, recall, AUC-ROC, Cohen's Kappa, and prediction time per checkpoint. Compare against logistic regression and a simple rule (for example, "missed one checkpoint means flagged").

**Risks.** The real dataset will be small. Mitigation: use a clearly labeled simulator for extra events and present the results as a pilot.

**Difficulty.** Moderate. The full-stack work makes this a good software engineering project even though the model itself is familiar.

---

## Proposal 2: Diacritical Mapping for Text-to-Speech

**Problem.** Many languages are written without diacritics in everyday text (Vietnamese typed without tone marks, Filipino without stress marks, Arabic without short vowels). Text-to-speech engines then mispronounce words, because one spelling can map to several pronunciations.

**Solution.** A tool that takes plain text or script files and returns the same text with diacritical marks restored, ready for a text-to-speech engine. It includes a side-by-side viewer and an audio preview using an open-source speech engine.

**Algorithm.** Treat it as character-level sequence labeling: for each base character, predict which diacritic it carries. Use a BiLSTM or a small Transformer encoder with a context window, and combine it with a dictionary lookup. The dictionary handles common words and the model handles unseen ones. Baseline: the most frequent marked form of each word.

**Data.** The cheapest way to get training data is to take correctly marked text, strip the marks automatically, and train the model to put them back. Vietnamese Wikipedia is large and well suited for building and validating the pipeline. Filipino stress marking is a stretch goal, since marked Filipino text is scarce and a dictionary source must be confirmed first. Pick the target language early, because it drives everything else.

**Core features.**

- Text and file input, with batch processing
- Marked output with a confidence score per word and highlighting for low-confidence words
- Manual correction that feeds a user dictionary
- Audio preview and export of the marked script

**SE deliverables.** Module diagram (preprocessing, model, dictionary, UI), API contract, a regression test suite of tricky word pairs, and model versioning.

**Evaluation.** Character-level accuracy, word-level accuracy, and accuracy on ambiguous words specifically. Optionally, a small listening test where people rate pronunciation.

**Risks.** Language choice and data scarcity. Mitigation: build on Vietnamese first and treat other languages as extensions.

**Difficulty.** Moderate-High. Training is modest, but designing the evaluation and handling the language details take care.

---

## Proposal 3: Pocket Almanac for Plants and Animals

**Problem.** People photograph plants and animals but cannot tell what they are or whether a plant looks healthy. Existing apps need a constant internet connection and rarely say anything about condition.

**Solution.** A handheld-friendly app that identifies a photographed species and shows basic information, an approximate life stage, and a health indicator. Every capture is saved to a personal collection, similar to a Pokedex.

**Algorithm.** Transfer learning with a lightweight CNN (MobileNetV3 or EfficientNet-Lite), exported to TensorFlow Lite so it runs on the phone without internet. Use separate models or heads for species, life stage, and plant health.

**Scope.** Estimating exact age from a photo is not realistic. Define it as an approximate **life stage** (for example seedling, mature, or flowering for plants; juvenile or adult for animals). Plant health is feasible through leaf condition (PlantVillage-style labels) and should be shown as an indicator, not a diagnosis. Animal health from a single photo is weak, so either drop it or limit it to clear visible cues.

**Data.** iNaturalist open subsets for species (choose 30 to 50 locally common species), PlantVillage for leaf disease, and an offline species information table written by the team.

**Core features.** Camera capture, offline identification, confidence display with a "not sure" fallback, a collection screen, and species detail pages.

**SE deliverables.** Mobile app architecture, model packaging pipeline, offline storage design, and a usability test with a few real users.

**Evaluation.** Top-1 and top-3 accuracy, per-class confusion analysis, and inference time on a mid-range phone.

**Risks.** Overpromising on age and health. Mitigation: a narrow species list, clear confidence thresholds, and honest wording in the interface.

**Difficulty.** Moderate-High, because of the mobile packaging on top of the model work.

---

## 🔴 Proposal 4: Fire Risk Mapper from Aerial Imagery

> 🔴 **Not considered.** Dropped by the team.

**Problem.** Dense neighborhoods with closely packed buildings, narrow roads that block fire trucks, and flammable materials are hard to assess across a whole city, and manual inspections are slow.

**Solution.** A map-based tool that analyzes aerial imagery of an area and highlights zones that are more vulnerable to fire, ranked for inspectors or barangay officials.

**Algorithm.** Two stages. First, extract features from imagery: building density, roof material class, vegetation near buildings, and road width. Use a CNN classifier or a pretrained segmentation model for buildings and roads. Second, combine those features into a transparent risk score using gradient boosting or a weighted scoring function, checked against known incident locations if available.

**Data note.** Google Maps imagery has terms of service that restrict scraping and bulk analysis. Check the terms before committing. Safer options are OpenStreetMap building and road data, Mapillary street-level imagery, open aerial datasets, or Sentinel imagery, with Google Maps used only to display results. Confirm the choice with the instructor early.

**Core features.** Area selection on a map, a risk heat map overlay, a ranked list of high-risk grid cells, an explanation of why a cell scored high, and report export.

**SE deliverables.** Geospatial data pipeline, grid or tile processing design, map interface, and reproducible processing scripts.

**Evaluation.** Classification accuracy on labeled imagery, and agreement with any historical incident data that can be obtained (even a small sample from a local fire station).

**Risks.** Labels for fire vulnerability are subjective and ground truth is hard to get. Mitigation: use an explainable score and present the output as screening support, not a prediction of actual fires.

**Difficulty.** Moderate-High, because of the geospatial and imagery pipeline.

---

## 🔴 Proposal 5: Habit and Addiction Risk Self-Monitor

> 🔴 **Not considered.** Dropped by the team.

**Problem.** People often do not notice that a habit such as heavy social media use or substance use is escalating until they are already dependent. Most self-awareness tools are simple counters with no sense of trend.

**Solution.** A private self-tracking app where users log or import their usage (screen time, session counts, late-night use, mood, substance frequency) and get a trend-based risk indicator with gentle, non-judgmental feedback. It is a self-awareness tool and must not claim to diagnose anything.

**Algorithm.** Feature engineering over time windows (weekly trend, share of night-time use, rate of escalation, spikes after a reduction), then logistic regression for interpretability and gradient boosting for comparison. Labels can come from an established short screening scale, such as the Bergen Social Media Addiction Scale for social media. The team should consult a guidance counselor or faculty adviser.

**Data.** Long-term addiction outcomes cannot be collected in a class project. Use a consented survey of volunteers (scale scores as labels) together with a documented synthetic data generator for testing the pipeline. State clearly that predictions are exploratory.

**Ethics.** This proposal handles sensitive data. Requirements include informed consent, local-only or encrypted storage, no data sharing, clear disclaimers, and an easy path to professional help resources. Compliance with the Data Privacy Act should be a written requirement from the start.

**Core features.** A quick daily log, trend charts, a risk indicator with an explanation, goal setting, and privacy controls (export and delete all data).

**SE deliverables.** Privacy and security requirements, threat model, consent flow, and data retention design.

**Evaluation.** Agreement between the model and screening-scale categories on the survey data, plus a usability and trust assessment with a small group.

**Risks.** Harm from misleading output and from handling sensitive data. Mitigation: cautious wording, adviser review, and collecting as little data as possible.

**Difficulty.** Moderate technically, but the ethics and validation work are the hard parts.

---

## Proposal 6: Laguna Tourism Itinerary Planner

**Problem.** Tourists and locals planning a day trip in Laguna have to juggle opening hours, travel time between places, budget, and interests across scattered sources. The tourism inquiry already provides real user needs and pain points to design against.

**Solution.** A web app that takes interests, budget, available hours, and a starting point, then builds a workable day itinerary and lets the user swap stops.

**Algorithm.** Model it as a time-limited route problem (an orienteering problem with time windows): maximize the total interest score within the time and budget limits. Solve it with a greedy build plus local search improvement, or with Google OR-Tools. Add a simple content-based recommender (tag matching with weights learned from user ratings) to score places.

**Data.** A team-curated database of 40 to 80 Laguna places with coordinates, tags, costs, opening hours, and visit durations. Travel times come from a routing API, with distance-based estimates as a fallback.

**Core features.** Preference form, generated itinerary with a map and timeline, regenerate and swap stops, and save and share.

**SE deliverables.** Requirements drawn from the inquiry findings, an algorithm module with unit tests, a map interface, and usability testing.

**Evaluation.** Constraint satisfaction rate, itinerary score compared with a manual plan and a random baseline, and user satisfaction ratings.

**Difficulty.** Moderate. Well-scoped and grounded in research the team already did.

---

## Proposal 7: KampusKonek Task Risk Predictor and Workload Balancer

**Problem.** KampusKonek keeps events, delegated tasks, deadlines, and adviser approvals in one place, but it only reports status after the fact. Officers learn a task is late when it already shows as overdue, adviser approvals can sit in the queue unnoticed, and some officers carry many open tasks while others carry none. The platform records what is needed to warn people earlier, but it does not use that data yet.

**Solution.** A prediction layer added on top of the existing KampusKonek (HTML, CSS, JavaScript, PHP, MySQL). It scores every open task for overdue risk, estimates how long each pending adviser request will wait, shows an event readiness score beside the current progress bar, and suggests a fair assignee when an officer delegates a task. The model runs as a small Python service that PHP calls over a REST endpoint. If the service is down, KampusKonek falls back to simple deadline rules and keeps working.

**Algorithm.**

- **Overdue risk:** a gradient boosting classifier (XGBoost or LightGBM) that gives the probability a task misses its deadline, compared against logistic regression and a deadline-rule baseline. Features: priority, days between creation and deadline, days remaining, restricted flag, approval status, assignee's open task count, assignee's past on-time rate, seat in the organization, days until the event, and days since the last status change.
- **Approval turnaround:** a gradient boosting regressor that predicts the hours until the adviser acts, using request type, queue length, day of week, and the adviser's recent response times.
- **Event readiness:** a transparent weighted score that combines task risks by priority and time left, so it can be explained to officers without a model.
- **Assignee suggestion:** score each candidate by predicted on-time probability minus a workload penalty, then assign several new tasks at once with the Hungarian algorithm (`scipy.optimize.linear_sum_assignment`).

**Data.** The current six tables (users, organizations, org_members, events, tasks, announcements) hold only the latest state. The project therefore adds a `task_status_log` table (task, old status, new status, time, who changed it) plus created, approved, and completed timestamps on tasks and events. Real history will be small at first, so the team builds a documented simulator of a student council (several organizations, events, officers with different habits, deadline pressure, adviser delays) to produce roughly 2,000 to 3,000 task records, and adds real records from a pilot with one council if the school allows. Synthetic data is labeled as such in every result, because a model trained on a simulator learns the simulator's rules.

**Core features.**

- Low, medium, or high risk badge on each task with the top two reasons (for example, "due in 2 days, assignee has 6 open tasks")
- "At risk" filter on the task board and a risk-sorted adviser approval queue showing expected wait
- Event readiness bar next to the existing progress bar
- Suggested assignee when creating a task, with a manual override
- Admin analytics page for workload spread and average approval time

**SE deliverables.** Schema migration script, REST contract between PHP and the Python service (with request and response examples), role rules for who may see risk scores, unit tests for feature building, role-by-role integration tests, a fallback behavior test, and updates to the User Manual and Developer Guide.

**Evaluation.** Use a time-ordered split (train on earlier events, test on later ones) so the model never sees the future. Report F1, recall, and AUC-ROC for overdue risk against the deadline-rule baseline; mean absolute error in hours for approval turnaround; precision at the top 5 risky tasks per event; and a short usability test where officers rate whether the warnings are clear and useful.

**Risks.** Little real data, and the risk that flags feel like judgments of people. Mitigation: label synthetic results clearly, frame the project as a pilot, show risk on tasks (never a "reliability ranking" of officers), and keep the officer's manual override.

**Difficulty.** Moderate. It extends a system the team already built, so most of the effort is integration, data design, and testing, with a manageable modeling component.

---

## Proposal 8: Campus Queue Wait-Time Predictor

**Problem.** Students line up at the registrar, cashier, and clinic without knowing how long they will wait, and offices cannot see demand patterns to schedule staff.

**Solution.** A system where queue joins and completions are logged (by QR scan or a kiosk tap), and students can see an estimated wait time before going to the office. Staff see demand forecasts by hour and day.

**Algorithm.** Combine a queueing-theory estimate (current queue length divided by the recent service rate) with a regression model (gradient boosting) that uses hour, weekday, academic calendar period (enrollment week, payment deadlines), and current queue length to predict the wait. Forecast hourly demand with a simple time-series method such as seasonal naive or Prophet-style decomposition.

**Data.** Self-collected counts at one or two offices over several days, plus a simulator calibrated on those counts to generate longer histories.

**Core features.** Queue join and completion logging, live estimated wait display, a peak-hour forecast chart for staff, and historical analytics.

**SE deliverables.** Real-time update design, data model for queue events, simulation module, and monitoring and test plan.

**Evaluation.** Mean absolute error of the predicted wait in minutes, compared against the simple queue-length baseline.

**Difficulty.** Moderate.

---

## Recommendation

For a balance of attainable and substantial:

- **Safest strong choice:** Proposal 1. The team already knows the domain, and the full-stack scope is rich. To keep it distinct from plain churn classification, lean on the survival-style second output and on engineering depth (testing, load, deployment).
- **Best technical showcase:** Proposal 2 or Proposal 3, as long as the scope is locked (one language, or 30 to 50 species).
- **Lower-risk build with solid design content:** Proposal 6 or Proposal 7. Proposal 7 reuses the existing KampusKonek system.
- 🔴 **Not considered:** Proposals 4 and 5, dropped by the team.

Whichever proposal is chosen, confirm the data source and the evaluation plan in the first week. The data question decides feasibility more than the algorithm does.