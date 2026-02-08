# Classical Machine Learning — Geometry, Probability & Optimization

> A **conceptually complete, math-heavy guide** to Classical Machine Learning that builds **true understanding** through unified perspectives on geometry, probability, and optimization.
>
> ## 🎯 What's Inside
>
> This repository provides a structured path through classical ML, moving from simple linear models to complex ensembles and probabilistic systems. Every chapter is **self-contained yet cumulative**, building geometric intuition, then probability concepts, then optimization techniques.
>
> ### Core Unifying Themes
>
> - **Geometry** — Vectors, projections, margins, subspaces
> - - **Probability** — Uncertainty, likelihoods, latent variables, Bayes
>   - - **Optimization** — Loss surfaces, convexity, gradient descent, EM
>    
>     - ---
>
> ## 📚 Repository Structure
>
> This repository is organized into **5 coherent parts**, each with multiple chapters. Start at PART 1 and progress sequentially—each section builds on previous concepts.
>
> ### **PART 1: Linear Models & Geometry Foundations**
> *Build foundational geometric intuitions for all of ML*
>
> - **[`01-linear-models-geometry/`](./01-linear-models-geometry/)**
> -   - `01-linear-regression/` — Vectors, projections, least squares, bias-variance
>     -   - `02-logistic-regression/` — Extending geometry to probabilities, cross-entropy
>      
>         - Why first? Linear Regression teaches you **vector spaces and loss surfaces**. Logistic Regression **bridges deterministic and probabilistic thinking**.
>      
>         - ---
>
> ### **PART 2: Margin-Based Learning**
> *Shift from probability to pure geometry with margins*
>
> - **[`02-margin-based-learning/`](./02-margin-based-learning/)**
> -   - `03-svm/` — Support Vector Machines, kernel trick, duality, margins
>  
>     - Why here? After linear models, SVMs show how to think geometrically about **robustness through margins**, without explicit probabilities.
>  
>     - ---
>
> ### **PART 3: Tree-Based Models & Ensembles**
> *Break linear geometry and learn variance + bias reduction*
>
> - **[`03-tree-ensembles/`](./03-tree-ensembles/)**
> -   - `04-decision-trees/` — Trees, impurity, information gain, axis-aligned splits
>     -   - `05-random-forests/` — Variance reduction through averaging
>         -   - `06-boosting/` — Bias reduction, functional gradient descent, AdaBoost → GBM
>             -   - `07-xgboost-lightgbm-catboost/` — Industrial-strength implementations with explicit regularization
>              
>                 - Why this order? Trees break linear structure. Random Forests reduce **variance**. Boosting reduces **bias**. XGBoost shows modern optimization with second-order geometry.
>              
>                 - ---
>
> ### **PART 4: Dimensionality Reduction & Representation**
> *Learn how to find meaningful lower-dimensional structure*
>
> - **[`04-dimensionality-reduction/`](./04-dimensionality-reduction/)**
> -   - `08-pca/` — Principal Component Analysis, eigenvalues, variance, subspaces
>     -   - `09-lda-ica-kernel-pca/` — LDA (supervised), ICA (independent), Kernel PCA (nonlinear)
>         -   - `10-manifold-learning/` — t-SNE, UMAP, topology, visualization
>          
>             - Why this order? PCA teaches **eigenstructure**. LDA/ICA show **different notions of "important direction"**. Manifold learning handles **nonlinear structure** for discovery and visualization.
>          
>             - ---
>
> ### **PART 5: Probabilistic Models & Latent Variables**
> *Combine probability, geometry, and optimization—bridge to deep learning*
>
> - **[`05-probabilistic-models/`](./05-probabilistic-models/)**
> -   - `11-bayesian-methods/` — Bayesian Decision Theory, Naive Bayes, optimal decisions under uncertainty
>     -   - `12-gmm-em/` — Gaussian Mixture Models, Expectation-Maximization algorithm
>      
>         - Why last? GMM + EM **unifies everything**: probability (likelihood), geometry (covariances, responsibilities), optimization (EM alternation). This directly prepares you for VAEs, diffusion models, and modern generative AI.
>      
>         - ---
>
> ## 🧠 How to Study This Repository
>
> ### ✅ Do This
>
> 1. **Follow the recommended order** — Start at PART 1, read sequentially within each part
> 2. 2. **Read the chapter READMEs first** — Each chapter folder has a `README.md` explaining its concepts
>    3. 3. **Derive equations on paper** — Don't just read; re-derive on a whiteboard
>       4. 4. **Visualize geometry** — Draw the concepts (projections, margins, decision boundaries, manifolds)
>          5. 5. **Revisit earlier chapters** — As you learn new models, see how they relate back to linear models
>            
>             6. ### ❌ Don't Do This
>            
>             7. - Don't skip to advanced topics
>                - - Don't memorize formulas without understanding derivations
>                  - - Don't ignore the "why" behind concepts
>                    - - Don't rush through geometry—it's the foundation
>                     
>                      - ---
>
> ## 🔁 Alternative Reading Paths
>
> ### Interview-Oriented
> Focus on practical models:
> Linear Regression → Logistic Regression → SVM → Decision Trees → Random Forests → XGBoost
>
> ### Probability-First
> If you're coming from statistics:
> Bayesian Decision Theory → Naive Bayes → GMM & EM → PCA → then explore others
>
> ### Deep Learning Preparation
> To prepare for neural networks:
> All PART 1 → PART 3 (especially boosting) → PART 4 (PCA for representations) → PART 5 (GMM/EM bridge to VAEs)
>
> ---
>
> ## 🧩 How This Connects to Deep Learning
>
> This classical ML foundation directly prepares you for:
>
> - **Backpropagation** comes from gradient boosting's functional gradient ideas
> - - **VAEs** (Variational Autoencoders) extend GMM + EM to deep networks
>   - - **Representation Learning** builds on PCA, kernels, and manifold structure
>     - - **Modern Optimization** (Adam, etc.) extends boosting's per-parameter adaptive learning
>      
>       - **Deep learning extends classical ML, doesn't replace it.** A deep understanding here makes modern methods feel natural, not magical.
>      
>       - ---
>
> ## ✨ Final Advice
>
> > **If you truly understand this repository, modern ML will feel intuitive.**
> >
> > - **Re-derive everything** — Use pencil and paper, don't just read
> > - - **Visualize aggressively** — Draw projections, margins, decision boundaries
> >   - - **Ask "why?"** — For every formula, understand the geometric or probabilistic intuition
> >     - - **Revisit chapters** — Early chapters take on new meaning as you learn later material
> >      
> >       - ---
> >
> > ## 📖 Chapter Index Quick Links
> >
> > | Chapter | Topic | Key Ideas |
> > |---------|-------|-----------|
> > | 01 | Linear Regression | Projections, least squares, bias-variance tradeoff |
> > | 02 | Logistic Regression | Log-odds, cross-entropy, convex optimization |
> > | 03 | SVM | Margins, duality, kernel trick |
> > | 04 | Decision Trees | Impurity, splitting, information gain |
> > | 05 | Random Forests | Bootstrap aggregation, variance reduction |
> > | 06 | Boosting | Functional gradients, bias reduction |
> > | 07 | XGBoost/LightGBM | Second-order optimization, regularization |
> > | 08 | PCA | Eigendecomposition, subspaces, variance |
> > | 09 | LDA/ICA/Kernel PCA | Supervised/independent/nonlinear projections |
> > | 10 | Manifold Learning | t-SNE, UMAP, topology, visualization |
> > | 11 | Bayesian Methods | Decision theory, Naive Bayes |
> > | 12 | GMM & EM | Latent variables, expectation-maximization |
> >
> > ---
> >
> > ## 🎓 Who Should Use This
> >
> > ✅ **Data Scientists** wanting deep mathematical foundations
> > ✅ **ML Engineers** preparing for technical interviews
> > ✅ **Researchers** needing clean conceptual structures
> > ✅ **Everyone** who wants to understand ML intuitively, not just use libraries
> >
> > ❌ **Not** for quick recipes or skipping to production code
> >
> > ---
> >
> > ## 📝 License
> >
> > This repository is educational material. Feel free to fork, share, and build upon it.
> >
> > ---
> >
> > **Happy learning!** 🌱
> >
> > *Start at PART 1. Progress sequentially. Re-derive on paper. Visualize constantly. You'll emerge with genuine understanding.*
