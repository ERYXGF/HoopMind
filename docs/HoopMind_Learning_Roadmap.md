# HoopMind: The 100-Step Build-As-You-Learn Roadmap

**Learn and build in parallel.** Every step below has two parts:
- 📚 **Learn:** the concept to study
- 🔨 **Build:** the file you create in your `hoopmind/` repo, or a basketball-themed exercise that builds the muscle

By step 100, you'll have a shippable product *and* the knowledge to maintain it. Early steps produce practice files (in a `hoopmind/sandbox/` folder); from Phase 4 onward, you're building the real product.

**Repo structure to set up on Day 1:**
```
hoopmind/
├── sandbox/          # learning exercises (Phases 1-3)
├── core/             # the real simulator (Phases 4+)
├── brain/            # Python ML server
├── unity/            # Unity project (Phase 8+)
├── data/             # basketball datasets
├── notebooks/        # exploration only
├── tests/
└── docs/
```

---

## Phase 1: Programming Foundations (Steps 1–10)

1. **Python basics** — variables, types, control flow, functions.
   - 📚 Official Python tutorial, chapters 1–4.
   - 🔨 `sandbox/01_player_stats.py` — store a player's name, points, rebounds, assists in variables and print a stat line.

2. **Python data structures** — lists, dicts, sets, tuples.
   - 📚 When to use each; their time complexity.
   - 🔨 `sandbox/02_roster.py` — represent a 5-player roster as a list of dicts. Compute team totals.

3. **Object-Oriented Programming** — classes, inheritance, dunder methods.
   - 📚 Python OOP tutorial.
   - 🔨 `sandbox/03_player_class.py` — build a `Player` class with attributes (position, height, skills) and a `__repr__`. Subclass into `PointGuard`, `Center`, etc.

4. **Functional patterns** — comprehensions, generators, decorators.
   - 📚 Real Python's articles on each.
   - 🔨 `sandbox/04_possessions.py` — generate 1000 fake possessions with a generator. Use a list comprehension to filter shots > 20 feet.

5. **Error handling & debugging** — try/except, logging, pdb.
   - 📚 Python docs on exceptions and logging.
   - 🔨 `sandbox/05_safe_stats.py` — load a CSV that may have missing values; handle the errors gracefully. Use `logging`, not `print`.

6. **Git & GitHub** — branches, PRs, .gitignore.
   - 📚 The "Pro Git" book, chapters 1–3.
   - 🔨 **Create the `hoopmind` repo on GitHub.** Push everything so far. Open one PR to yourself just to practice the flow.

7. **Command line / Bash** — piping, grep, ssh.
   - 📚 "The Missing Semester" lecture 1–2 (MIT).
   - 🔨 `sandbox/06_logs.sh` — a bash script that tails a fake game log and greps for "made shots."

8. **Virtual environments & dependency management** — venv, pip, uv.
   - 📚 Python packaging guide.
   - 🔨 Create `hoopmind/requirements.txt` and a working venv. Document setup in `README.md`.

9. **Writing tests** — pytest, fixtures.
   - 📚 pytest's "Get Started" docs.
   - 🔨 `tests/test_player_class.py` — write 5 tests for your `Player` class from step 3.

10. **Reading other people's code** — trace a real codebase.
    - 📚 Pick a small RL repo on GitHub (e.g., a tic-tac-toe Q-learning agent).
    - 🔨 `docs/code_walkthrough.md` — write a 1-page explanation of how that repo works.

---

## Phase 2: Mathematics for ML (Steps 11–20)

11. **Linear algebra fundamentals** — vectors, matrices, dot products.
    - 📚 3Blue1Brown "Essence of Linear Algebra," videos 1–4.
    - 🔨 `sandbox/11_court_vectors.py` — represent player positions as 2D vectors. Compute distance between players using dot products.

12. **Linear algebra applied** — eigenvalues, decomposition.
    - 📚 3Blue1Brown videos 5–14.
    - 🔨 `sandbox/12_shot_chart_pca.py` — apply PCA (via NumPy) to a fake shot-location dataset to find the dominant axis of attack.

13. **Calculus — derivatives** — chain rule, partial derivatives.
    - 📚 3Blue1Brown "Essence of Calculus," videos 1–4.
    - 🔨 `sandbox/13_chain_rule.py` — implement numerical and analytical derivatives of `f(x) = (3x + 2)^2` and verify they match.

14. **Calculus — gradients & optimization** — gradient descent intuition.
    - 📚 3Blue1Brown videos 5–10.
    - 🔨 `sandbox/14_gradient_descent.py` — minimize a 2D loss surface by hand-coded gradient descent. Plot the path.

15. **Probability basics** — distributions, expectation, variance.
    - 📚 Khan Academy's probability unit.
    - 🔨 `sandbox/15_shot_distribution.py` — model free-throw success as a Bernoulli distribution. Simulate 10,000 attempts; compare empirical mean to theoretical.

16. **Probability for ML** — Bayes, KL divergence.
    - 📚 StatQuest videos on Bayes' theorem and KL divergence.
    - 🔨 `sandbox/16_bayes_clutch.py` — given P(clutch shot made | star player) and priors, compute the posterior.

17. **Statistics** — sampling, hypothesis testing.
    - 📚 StatQuest's hypothesis testing playlist.
    - 🔨 `sandbox/17_ab_test.py` — given two players' shooting %s over N attempts, test whether the difference is statistically significant.

18. **Information theory primer** — entropy, cross-entropy.
    - 📚 Chris Olah's "Visual Information Theory" blog post.
    - 🔨 `sandbox/18_entropy.py` — compute entropy of a team's play-call distribution. Predictable team = low entropy.

19. **Discrete math touch-ups** — graphs, combinatorics.
    - 📚 Any "Discrete Math for CS" intro.
    - 🔨 `sandbox/19_play_tree.py` — represent a basketball play as a tree (nodes = decisions, edges = passes). Traverse it.

20. **NumPy fluency** — broadcasting, vectorization.
    - 📚 NumPy's official "Absolute Beginners" guide + "Broadcasting" doc.
    - 🔨 `sandbox/20_numpy_court.py` — represent the court as a 94×50 NumPy array. Vectorize a function that computes distance from every cell to the rim.

---

## Phase 3: Data Tooling (Steps 21–27)

21. **Pandas** — DataFrames, groupby, merge.
    - 📚 "10 Minutes to pandas" + Kevin Markham's videos.
    - 🔨 `sandbox/21_pandas_stats.py` — load a CSV of NBA player season stats; compute team PPG with groupby.

22. **Matplotlib & Seaborn** — plotting.
    - 📚 Matplotlib's "Pyplot tutorial."
    - 🔨 `sandbox/22_shot_chart.py` — plot a shot chart with court markings as a background.

23. **Jupyter notebooks** — for exploration only.
    - 📚 Jupyter quickstart.
    - 🔨 `notebooks/23_exploration.ipynb` — re-do steps 21–22 in a notebook. Note how it differs from `.py` files.

24. **Working with JSON & APIs** — `requests`, nested parsing.
    - 📚 Real Python's "API Integration in Python."
    - 🔨 `sandbox/24_api_pull.py` — pull live data from the free `balldontlie` API for one player.

25. **SQL basics** — SELECT, JOIN, GROUP BY.
    - 📚 SQLZoo or Mode's SQL tutorial.
    - 🔨 `sandbox/25_games.db` — create a SQLite database with `players`, `games`, `shots` tables. Write 5 queries.

26. **File formats for ML** — Parquet, HDF5, Pickle.
    - 📚 Pandas IO docs.
    - 🔨 `sandbox/26_format_benchmark.py` — save the same 1M-row DataFrame as CSV, Parquet, Pickle. Compare file size and load time.

27. **Real basketball data ingestion.**
    - 📚 `nba_api` GitHub README.
    - 🔨 `core/data/ingest.py` — **this is your first real `core/` file.** Pull and cache play-by-play data for one team's season. This data will fuel everything.

---

## Phase 4: Classical ML (Steps 28–37)

From here on, files go in `core/` — you're building the actual product.

28. **ML mental model** — features, labels, train/val/test.
    - 📚 Andrew Ng's "Machine Learning" Coursera, week 1.
    - 🔨 `core/data/dataset_splits.py` — split your play-by-play data into train/val/test with no temporal leakage.

29. **Linear regression from scratch.**
    - 📚 StatQuest's linear regression video.
    - 🔨 `core/models/linear_from_scratch.py` — predict shot success probability from distance using only NumPy.

30. **Logistic regression & classification.**
    - 📚 StatQuest's logistic regression video.
    - 🔨 `core/models/shot_classifier.py` — same task as step 29 but with logistic regression. Compare.

31. **Loss functions** — MSE, cross-entropy, hinge.
    - 📚 "Loss Functions Explained" (any decent blog).
    - 🔨 `core/losses.py` — implement MSE and binary cross-entropy in NumPy with unit tests in `tests/`.

32. **Gradient descent variants** — SGD, mini-batch.
    - 📚 Sebastian Ruder's "An overview of gradient descent."
    - 🔨 `core/optimizers/sgd.py` — implement SGD from scratch. Train your step-30 model with it.

33. **scikit-learn.**
    - 📚 sklearn's "Getting Started" guide.
    - 🔨 `core/models/sklearn_baseline.py` — train random forest and SVM on the shot-success task. Beat your from-scratch baseline.

34. **Evaluation metrics** — precision, recall, F1, ROC-AUC.
    - 📚 "Beyond Accuracy" by Boaz Shmueli (Medium).
    - 🔨 `core/evaluation/metrics.py` — implement all 5 metrics. Use them in `tests/test_metrics.py`.

35. **Feature engineering** — scaling, encoding, time features.
    - 📚 "Feature Engineering for Machine Learning" (O'Reilly excerpts).
    - 🔨 `core/data/features.py` — engineer 10 features from play-by-play (shot clock %, score differential, possession length, etc.).

36. **Bias-variance tradeoff.**
    - 📚 Andrew Ng's "Advice for Applying ML."
    - 🔨 `notebooks/36_learning_curves.ipynb` — plot learning curves for your shot model at different training sizes. Diagnose under- vs overfitting.

37. **Cross-validation & hyperparameter tuning.**
    - 📚 sklearn's model selection docs.
    - 🔨 `core/training/hyperparam_search.py` — grid-search a random forest's hyperparameters with 5-fold CV.

---

## Phase 5: Deep Learning Foundations (Steps 38–50)

38. **Perceptrons & feedforward networks.**
    - 📚 Michael Nielsen's "Neural Networks and Deep Learning," ch. 1.
    - 🔨 `core/models/mlp_numpy.py` — a 2-layer MLP in pure NumPy that predicts shot success.

39. **Activation functions.**
    - 📚 Nielsen ch. 1 (continued).
    - 🔨 Add ReLU, sigmoid, tanh to `mlp_numpy.py`. Compare convergence on the same task.

40. **Backpropagation by hand.**
    - 📚 Karpathy's "Yes, you should understand backprop."
    - 🔨 `docs/backprop_derivation.md` — derive backprop for your 2-layer net on paper, photograph it, drop it in docs.

41. **PyTorch basics.**
    - 📚 PyTorch "60-minute Blitz" tutorial.
    - 🔨 `core/models/mlp_torch.py` — port your NumPy MLP to PyTorch. Verify outputs match.

42. **Your first real PyTorch model.**
    - 📚 PyTorch's MNIST tutorial.
    - 🔨 `core/models/possession_outcome.py` — predict possession outcome (made FG / missed FG / turnover) from state features.

43. **Training loops.**
    - 📚 Karpathy's "A Recipe for Training Neural Networks."
    - 🔨 `core/training/trainer.py` — a reusable `Trainer` class with train/val/checkpoint logic.

44. **Optimizers** — SGD, Adam, etc.
    - 📚 Original Adam paper (skim) + Lilian Weng's optimizer blog.
    - 🔨 Sweep optimizers in `core/training/trainer.py`. Log which wins for your task.

45. **Regularization** — dropout, weight decay, BN.
    - 📚 The original Dropout paper.
    - 🔨 Add dropout + weight decay to `possession_outcome.py`. Re-plot learning curves.

46. **CNNs.**
    - 📚 Stanford CS231n notes, "Convolutional Networks."
    - 🔨 `core/models/court_cnn.py` — treat the court as a 2D image (player positions as heatmap channels); train a CNN to predict outcome.

47. **RNNs & LSTMs.**
    - 📚 Chris Olah's "Understanding LSTMs."
    - 🔨 `core/models/possession_lstm.py` — model a possession as a sequence of states; LSTM predicts the outcome from the sequence.

48. **Transformers.**
    - 📚 "The Illustrated Transformer" by Jay Alammar.
    - 🔨 `core/models/possession_transformer.py` — replace the LSTM with a small Transformer. Compare.

49. **Training infrastructure** — GPU, W&B.
    - 📚 W&B quickstart.
    - 🔨 Wire `wandb` into `trainer.py`. Train one model on Colab GPU. View the run dashboard.

50. **Reading papers.**
    - 📚 "Attention Is All You Need" + "Playing Atari with Deep RL."
    - 🔨 `docs/paper_notes/` — start a folder of 1-page paper summaries. Two to start.

---

## Phase 6: Reinforcement Learning (Steps 51–63)

This is the heart of HoopMind. From step 58 onward, you're training the real agents.

51. **RL formalism.**
    - 📚 Sutton & Barto, ch. 1–3 (free online).
    - 🔨 `docs/rl_glossary.md` — define agent, state, action, reward, policy, episode in your own words.

52. **MDPs & Bellman equation.**
    - 📚 Sutton & Barto, ch. 3.
    - 🔨 `sandbox/52_gridworld.py` — define a 4×4 gridworld MDP. Write down the Bellman equation for one state.

53. **Value functions.**
    - 📚 Sutton & Barto, ch. 3.5–3.6.
    - 🔨 Extend `52_gridworld.py` to compute V(s) by hand for a fixed policy.

54. **Dynamic programming** — policy/value iteration.
    - 📚 Sutton & Barto, ch. 4.
    - 🔨 `sandbox/54_value_iteration.py` — solve gridworld with value iteration.

55. **Monte Carlo methods.**
    - 📚 Sutton & Barto, ch. 5.
    - 🔨 `sandbox/55_monte_carlo.py` — estimate V(s) from rollouts only, no transition model.

56. **TD learning — Q-learning.**
    - 📚 Sutton & Barto, ch. 6.
    - 🔨 `sandbox/56_q_learning.py` — solve FrozenLake (gymnasium) with tabular Q-learning.

57. **Function approximation.**
    - 📚 Sutton & Barto, ch. 9 (skim).
    - 🔨 `sandbox/57_linear_q.py` — Q-learning with a linear function approximator on CartPole.

58. **Deep Q-Networks (DQN).**
    - 📚 Original DQN paper + CleanRL's `dqn.py`.
    - 🔨 `brain/agents/dqn.py` — **first file in the real `brain/` folder.** DQN on a custom 1v0 "drive to rim" environment.

59. **Policy gradients — REINFORCE.**
    - 📚 Sutton & Barto, ch. 13.1–13.3.
    - 🔨 `brain/agents/reinforce.py` — REINFORCE on the same 1v0 environment.

60. **Actor-Critic.**
    - 📚 Lilian Weng's "Policy Gradient Algorithms" blog.
    - 🔨 `brain/agents/a2c.py` — A2C on a 1v1 environment (one offender, one defender).

61. **PPO.**
    - 📚 Schulman et al.'s PPO paper + CleanRL's `ppo.py`.
    - 🔨 `brain/agents/ppo.py` — PPO on the 1v1 task. **This is the algorithm that ships.**

62. **Reward shaping.**
    - 📚 "Reward is enough" + "Faulty Reward Functions" (OpenAI).
    - 🔨 `brain/environments/rewards.py` — design 3 reward functions for basketball (sparse, dense, shaped). Document tradeoffs.

63. **Common RL pitfalls.**
    - 📚 Alex Irpan's "Deep RL Doesn't Work Yet."
    - 🔨 `docs/rl_pitfalls.md` — list the failure modes you've personally hit. Update as you encounter new ones.

---

## Phase 7: Multi-Agent RL (Steps 64–70)

64. **Multi-agent fundamentals.**
    - 📚 Albrecht et al., "Multi-Agent Reinforcement Learning" (free textbook), ch. 1–2.
    - 🔨 `brain/environments/two_v_two.py` — a 2v2 environment in pure Python (no Unity yet).

65. **Non-stationarity problem.**
    - 📚 Same textbook, ch. 5.
    - 🔨 Train 2 independent PPO agents in `two_v_two.py`. Observe instability. Document it in `docs/`.

66. **Centralized Training, Decentralized Execution.**
    - 📚 MADDPG paper.
    - 🔨 `brain/agents/maddpg.py` or refactor PPO into a CTDE setup.

67. **MAPPO.**
    - 📚 MAPPO paper (Yu et al.).
    - 🔨 `brain/agents/mappo.py` — MAPPO on 2v2. Compare to independent PPO.

68. **Self-play.**
    - 📚 "Emergent Complexity via Multi-Agent Competition" (OpenAI).
    - 🔨 `brain/training/self_play.py` — alternate training offense and defense against each other.

69. **Curriculum learning.**
    - 📚 Bengio et al., "Curriculum Learning."
    - 🔨 `brain/training/curriculum.py` — start 1v1, progress to 5v5 over training. Save checkpoints at each stage.

70. **Emergent behavior.**
    - 📚 OpenAI "Hide and Seek" paper.
    - 🔨 `docs/emergent_behaviors.md` — log any surprising tactics your agents develop. (This becomes great marketing content later.)

---

## Phase 8: C# and Unity (Steps 71–80)

You've validated the brain in Python. Now build the simulation.

71. **C# fundamentals.**
    - 📚 Microsoft's official C# tour.
    - 🔨 `unity/sandbox/01_PlayerStats.cs` — port your step-1 player stats exercise to C#.

72. **C# vs Python differences.**
    - 📚 "C# for Python developers" (any blog).
    - 🔨 `unity/sandbox/02_TypedRoster.cs` — port step 2; feel the difference of static typing.

73. **Unity basics.**
    - 📚 Unity's "Roll-a-Ball" tutorial.
    - 🔨 `unity/HoopMind/` — create the Unity project. Complete Roll-a-Ball *inside* this project (you'll delete it later).

74. **Unity scripting.**
    - 📚 Unity manual, "Creating and using scripts."
    - 🔨 `unity/HoopMind/Assets/Scripts/Ball.cs` — a basketball that you can move with arrow keys.

75. **Unity physics.**
    - 📚 Unity physics manual.
    - 🔨 Add Rigidbody + bounce physics to `Ball.cs`. Make it dribble realistically.

76. **Unity animation.**
    - 📚 Unity animation tutorials.
    - 🔨 Import a free humanoid model (Mixamo). Wire run + shoot + pass animations into an Animator Controller.

77. **3D math in Unity.**
    - 📚 "Math for Game Programmers" (GDC YouTube talks).
    - 🔨 `Assets/Scripts/CourtMath.cs` — utility functions: distance to rim, angle to basket, "is open" check via raycasts.

78. **Performance in Unity.**
    - 📚 Unity profiler docs.
    - 🔨 `docs/unity_performance.md` — profile a 10-player scene; document bottlenecks.

79. **Basketball court prototype.**
    - 📚 N/A (you have the skills now).
    - 🔨 `Assets/Scenes/Court.unity` — full court, two hoops, one ball, regulation dimensions. No AI yet.

80. **Unity UI — the command bubble.**
    - 📚 Unity UI Toolkit docs.
    - 🔨 `Assets/Scripts/UI/CommandBubble.cs` — the chat input that pauses the sim when open (your "Active Time Battle" mechanic).

---

## Phase 9: ML-Agents and the Brain–Unity Bridge (Steps 81–87)

81. **Unity ML-Agents Toolkit.**
    - 📚 ML-Agents docs, "Getting Started."
    - 🔨 Run the 3DBall example inside `unity/HoopMind/`. Train it. Watch it learn.

82. **Observations and actions in ML-Agents.**
    - 📚 ML-Agents docs, "Designing Agents."
    - 🔨 `Assets/Scripts/Agents/BasketballAgent.cs` — define a single agent's observation space (player + ball positions) and action space.

83. **Reward design in Unity (C# side).**
    - 📚 ML-Agents reward design docs.
    - 🔨 Port your `brain/environments/rewards.py` logic into `BasketballAgent.cs`. Keep them in sync.

84. **Training with ML-Agents.**
    - 📚 ML-Agents training config docs.
    - 🔨 `unity/config/hoopmind_ppo.yaml` — train one offensive agent against a scripted defender. Tensorboard the run.

85. **WebSocket fundamentals.**
    - 📚 MDN WebSocket docs + any FastAPI WebSocket tutorial.
    - 🔨 `brain/server/echo.py` + `unity/Assets/Scripts/Net/WebSocketClient.cs` — Unity sends "ping," Python replies "pong." Latency under 10ms.

86. **FastAPI.**
    - 📚 FastAPI's official tutorial.
    - 🔨 `brain/server/main.py` — FastAPI app with HTTP `/health` and a `/ws/game` WebSocket endpoint.

87. **The state→action JSON contract.**
    - 📚 JSON Schema basics.
    - 🔨 `docs/schemas/state_action_v1.json` — the formal schema. Versioned. Pydantic models in `brain/schemas.py`. C# types in `Assets/Scripts/Net/GameState.cs`.

---

## Phase 10: LLM Integration (Steps 88–92)

88. **LLM API fundamentals.**
    - 📚 Anthropic's API quickstart.
    - 🔨 `brain/llm/client.py` — wrap the API with retry/timeout. Hello-world a basketball joke.

89. **Prompt engineering for structured output.**
    - 📚 Anthropic's prompt engineering docs.
    - 🔨 `brain/llm/parse_command.py` — prompt that turns "set a back-screen for the SG" into JSON matching your schema.

90. **Function calling / tool use.**
    - 📚 Anthropic's tool-use docs.
    - 🔨 Refactor `parse_command.py` to use tool-use. Define every basketball action as a tool.

91. **Latency and cost management.**
    - 📚 Anthropic's caching docs.
    - 🔨 `brain/llm/cache.py` — cache common commands. Use Haiku for parsing, Sonnet for the post-game audit.

92. **Evaluating LLM outputs.**
    - 📚 "LLM-as-a-Judge" papers (skim).
    - 🔨 `tests/llm/test_command_parser.py` — 200 commands with expected JSON. Measure accuracy. Track regressions.

---

## Phase 11: MLOps and Deployment (Steps 93–97)

93. **Experiment tracking.**
    - 📚 W&B or MLflow tutorials.
    - 🔨 Wire W&B into every training script in `brain/`. Tag runs by experiment.

94. **Docker.**
    - 📚 Docker's official getting-started guide.
    - 🔨 `brain/Dockerfile` + `docker-compose.yml` — the brain server runs in a container locally.

95. **Cloud GPU training.**
    - 📚 Lambda Labs or Vast.ai quickstart.
    - 🔨 `scripts/cloud_train.sh` — spin up a GPU box, sync code, train, save checkpoints, tear down. Budget alerts on.

96. **Model versioning & serving.**
    - 📚 "ML Model Versioning Best Practices."
    - 🔨 `brain/serving/registry.py` — load a model by version tag. Swap models without restarting Unity.

97. **Observability.**
    - 📚 Structured logging tutorial.
    - 🔨 `brain/logging_config.py` + a `/metrics` endpoint. Alert when LLM parsing accuracy drops below 95%.

---

## Phase 12: Product, Polish, Marketability (Steps 98–100)

98. **User experience & playtesting.**
    - 📚 "The Art of Game Design" by Jesse Schell (the lens chapters).
    - 🔨 `docs/playtest_log.md` — run 5 playtests with real basketball fans. Record every confusion point. Iterate the tactical audit copy.

99. **Content creation as marketing.**
    - 📚 Pieter Levels' "Make book" or any indie devlog post-mortem.
    - 🔨 Start a `devlog/` — weekly post on X or YouTube from step 1. By step 100 you have ~2 years of content and an audience.

100. **Shipping and monetization.**
     - 📚 Steam's "Steamworks Documentation" + itch.io's seller guide.
     - 🔨 `STORE_PAGE.md` — Steam page copy, trailer script, pricing, EULA. Click publish.

---

## How to Pace Yourself

- **One step per 1–3 days** on average. Some (like step 61, PPO) will take a week. Some (like step 23, Jupyter) take an hour. That averages out.
- **Don't skip the 🔨 part.** Skipping the build is how you end up with a credential but no portfolio.
- **Commit every file.** Every single one. Even broken ones, on branches. Your commit history is proof of work.
- **Revisit `core/` and `brain/` files as you learn more.** Your step-29 linear regression will look embarrassing by step 50. Rewrite it. That rewrite *is* learning.
- **When stuck for >2 hours, search past chats or ask.** Don't burn a weekend on a bug a 10-minute question would solve.

Step 1 starts now. `mkdir hoopmind && cd hoopmind && git init`.
