# From an Abundance of Proof to an Abundance of Understanding

Luke Bailey\* · Kaiyue Wen\*

\* Co-first authors. Author order on the website is randomized on each page load.

We are approaching a strange situation in AI research. We have extraordinarily capable mathematical problem solvers. We also have extraordinarily capable experimentalists. Yet it is much less clear that we are getting a corresponding abundance of understanding.

## 1. Why understanding matters

We want to understand the world around us. Understanding helps us anticipate what will happen, decide what to do, and recognize when our expectations are wrong. It also has value beyond its usefulness. There is something deeply human about wanting to know why the world behaves as it does.

One way to think about understanding is the ability to make accurate predictions. We are especially interested in out-of-distribution (OOD) prediction: using an explanation to predict what happens in settings that differ from those in which it was developed. When we understand a system in this sense, its behavior under new conditions becomes less surprising.

Consider the Euler equations, which describe fluid motion under idealized assumptions. Water is familiar, yet its behavior can be extraordinarily complicated. Writing down the equations gives us rules for how a flow evolves. Understanding those rules means being able to say what kinds of behavior they allow and under what conditions.

For example, can a flow that begins smooth develop a singularity—a breakdown of that smoothness—under the equations? Our everyday experience of water does not settle the question. The equations let us formulate it precisely, but answering it requires more than knowing the equations themselves.

This is a distinction we care about: specifying a system is one step toward understanding its behavior. We also need concepts that help us reason about what follows from that specification.

## 2. How well do we understand deep learning?

In our own field, deep learning, this distinction is hard to ignore. We know how neural networks are trained. We specify the network’s architecture, the objective it learns to optimize, and the algorithm that updates its parameters. We can write down how one training step produces the next.

Yet many of the questions we care about remain difficult to answer. How do useful internal representations form? Why does a model perform well on examples it was not trained on? How do the architecture and training algorithm affect the solution it learns? Which conclusions from a small experiment will survive at a much larger scale?

We do have some understanding. Scaling laws describe how performance changes with quantities such as model size, data, and computation. In some settings, we can transfer training choices from small models to larger ones. We have useful intuitions about what models learn and some ability to predict experimental outcomes.

But that understanding is fragmented. A prediction works only after we settle a long list of details. An explanation is convincing in one setting, but its relevance to another is unclear. Two papers appear to disagree, and resolving the disagreement requires reconstructing much of the investigation.

Our guess is that we need better abstractions: concepts that organize observations, identify which details matter, and support predictions in new situations. We have become familiar with many remarkable phenomena in deep learning. We would like to understand them well enough that fewer of them take us by surprise.

## 3. Accelerating understanding with AI agents and humans

We believe understanding can be characterized by the efficiency of prediction in out-of-distribution (OOD) settings: how efficiently an explanation lets us make accurate predictions beyond the settings in which it was developed. This gives us a route to evaluating understanding. It also gives agents and humans a quantitative objective to hill-climb, iteratively proposing, testing, and refining explanations to improve OOD prediction efficiency.

Perhaps models already have much of the capability needed to turn experimental observations into understanding. What we may lack is a framework that directs their mathematical and experimental abilities toward that goal. We can provide agents with research questions and a research environment in which to investigate them. The agents will use this environment to run experiments, examine evidence, and develop abstractions and explanations of the phenomena they study.

We will then evaluate those abstractions and explanations in held-out OOD settings that were not used to develop them. The objective is concrete: given a computational budget in an OOD setting, minimize prediction error in that setting.

This framework naturally extends to evaluating human theoretical understanding. We can use theories and explanations proposed by human researchers to make predictions in held-out OOD settings, then measure their prediction error under a given computational budget in those settings. This gives us a common criterion for evaluating understanding, whether it comes from humans or agents.

We do not know how much scaffolding this would require. Given how capable the models already are, perhaps less than we expect. We want to gather fundamental questions in our field and use this process to build a stronger foundation for understanding deep learning.

## 4. Why do this in the open?

We expect AI capabilities to keep improving even while human understanding remains incomplete. AI may become increasingly good at finding ways to improve AI. Better systems alone would not ensure that the knowledge needed to understand them becomes widely available.

But we would find it deeply troubling—and sad—if the best understanding accumulated inside a few large labs while the rest of the world was left with incomplete or contradictory accounts.

Imagine living through the rise of steam power, watching engines transform factories and transportation. Now suppose the companies building those engines understood thermodynamics—the principles governing heat, work, and energy—but kept that knowledge to themselves. Everyone else continued to reason using phlogiston, a supposed substance released during combustion, without access to the evidence needed to replace that theory. The engines might keep improving, but the public would lack the foundations to understand them, question the prevailing explanations, or build on that knowledge independently.

Now imagine those companies asking society to commit resources equivalent to 10% of the country’s GDP to build a super steam engine. The public needs to know how likely its boiler is to explode, what evidence supports that estimate, and how uncertain it is. People are being asked to bear both the cost and the risk. Without access to the knowledge and evidence needed to assess that risk, how could they make an informed decision about whether to build it, or what conditions to place on its operation?

The same concern applies to AI. Suppose someone asks to train a model 100 times larger. Without understanding how scale affects capabilities, how could we judge what we were agreeing to, or whether the result would remain within the limits we intended to set? Meaningful public control requires enough understanding to assess what a proposed change could do and to question the evidence offered for it.

Understanding lets us get to know our alien friends better, and could lead to a future where we work with them with greater clarity. It also has value beyond its usefulness. There is something worth preserving in the human ability to understand the systems shaping our world.

The open research community therefore has a role beyond keeping up with capabilities. We should make this knowledge available, testable, and possible to pass on to future generations—even if those generations do not need to understand every detail in order to build more capable AI.

We see this as an open-source effort to build a shared understanding of deep learning. Contributions could come from labs or individual researchers, with or without agents. They could take the form of an answer, a counterexample, a reproducible experiment, or a new question.

We want to help build that foundation, and we would be happy to talk with anyone interested in joining. As AI changes the world around us, we want the ability to understand it to be something we can share—and pass on.
