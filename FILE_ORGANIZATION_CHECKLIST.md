FILE ORGANIZATION CHECKLIST

This document maps every existing markdown file to its target location in the new directory structure.

PART 1: Linear Models and Geometry Foundations
Target: 01-linear-models-geometry/

Chapter 1: Linear Regression
Target Directory: 01-linear-models-geometry/01-linear-regression/

Existing Files to Move:
- 01_foundations_basics.md -> 01_foundations_basics.md
- - 01_foundations_mathematical_intuition.md -> 02_mathematical_foundations.md
  - - 01_foundations_real_world_scenarios.md -> 04_real_world_project_issues.md
    - - 01_foundations_tricky_questions.md -> 05_tricky_interview_questions.md
      - - 02_linear_regression_geometric_interpretation.md -> 02_geometric_interpretation.md
        - - 02_linear_regression_mathematical_derivations.md -> 03_mathematical_derivations.md
          - - 02_linear_regression_real_world_project_issues.md -> Merge with 04_real_world_project_issues.md
            - - 02_linear_regression_tricky_interview_questions.md -> Merge with 05_tricky_interview_questions.md
             
              - New Structure:
              - - 01_foundations_basics.md
                - - 02_mathematical_foundations.md
                  - - 03_mathematical_derivations.md
                    - - 04_real_world_project_issues.md
                      - - 05_tricky_interview_questions.md
                       
                        - Chapter 2: Logistic Regression
                        - Target Directory: 01-linear-models-geometry/02-logistic-regression/
                       
                        - Existing Files to Move:
                        - - 03_logistic_regression_basics.md -> 01_basics.md
                          - - 03_logistic_regression_geometric_interpretation.md -> 02_geometric_interpretation.md
                            - - 03_logistic_regression_mathematical_derivation.md -> 03_mathematical_derivation.md
                              - - 03_logistic_regression_real_world_project_issues.md -> 04_real_world_project_issues.md
                                - - 03_logistic_regression_tricky_interview_questions.md -> 05_tricky_interview_questions.md
                                 
                                  - New Structure:
                                  - - 01_basics.md
                                    - - 02_geometric_interpretation.md
                                      - - 03_mathematical_derivation.md
                                        - - 04_real_world_project_issues.md
                                          - - 05_tricky_interview_questions.md
                                           
                                            - PART 2: Margin-Based Learning
                                            - Target: 02-margin-based-learning/
                                           
                                            - Chapter 3: Support Vector Machines
                                            - Target Directory: 02-margin-based-learning/03-svm/
                                           
                                            - Files to Create:
                                            - - INDEX.md (awaiting content)
                                              - - 01_basics.md
                                                - - 02_geometry_and_kernels.md
                                                  - - 03_duality.md
                                                    - - 04_real_world_project_issues.md
                                                      - - 05_tricky_interview_questions.md
                                                       
                                                        - PART 3: Tree-Based Models and Ensembles
                                                        - Target: 03-tree-ensembles/
                                                       
                                                        - Regularization Foundation (Note on Structure):
                                                        - - 04_regularization_*.md files provide foundation for ensemble methods
                                                          - - Consider creating a 00-regularization-concepts/ folder OR
                                                            - - Distribute to relevant ensemble chapters
                                                             
                                                              - Chapter 4: Decision Trees
                                                              - Target Directory: 03-tree-ensembles/04-decision-trees/
                                                             
                                                              - Existing Files to Move:
                                                              - - 05_decision_trees_basics.md -> 01_basics.md
                                                                - - 05_decision_trees_geometric_interpretation.md -> 02_geometric_interpretation.md
                                                                  - - 05_decision_trees_impurity_and_splitting_math.md -> 03_impurity_and_splitting_math.md
                                                                    - - 05_decision_trees_real_world_project_issues.md -> 04_real_world_project_issues.md
                                                                      - - 05_decision_trees_tricky_interview_questions.md -> 05_tricky_interview_questions.md
                                                                       
                                                                        - New Structure:
                                                                        - - INDEX.md
                                                                          - - 01_basics.md
                                                                            - - 02_geometric_interpretation.md
                                                                              - - 03_impurity_and_splitting_math.md
                                                                                - - 04_real_world_project_issues.md
                                                                                  - - 05_tricky_interview_questions.md
                                                                                   
                                                                                    - Chapter 5: Random Forests
                                                                                    - Target Directory: 03-tree-ensembles/05-random-forests/
                                                                                   
                                                                                    - Files to Create:
                                                                                    - - INDEX.md
                                                                                      - - 01_bootstrap_aggregation.md
                                                                                        - - 02_variance_reduction_theory.md
                                                                                          - - 03_feature_importance.md
                                                                                            - - 04_real_world_applications.md
                                                                                              - - 05_interview_questions.md
                                                                                               
                                                                                                - Chapter 6: Boosting
                                                                                                - Target Directory: 03-tree-ensembles/06-boosting/
                                                                                               
                                                                                                - Files to Create:
                                                                                                - - INDEX.md
                                                                                                  - - 01_adaboost_basics.md
                                                                                                    - - 02_functional_gradient_descent.md
                                                                                                      - - 03_gradient_boosting_machines.md
                                                                                                        - - 04_real_world_issues.md
                                                                                                          - - 05_interview_questions.md
                                                                                                           
                                                                                                            - Chapter 7: XGBoost, LightGBM, CatBoost
                                                                                                            - Target Directory: 03-tree-ensembles/07-xgboost-lightgbm-catboost/
                                                                                                           
                                                                                                            - Files to Create:
                                                                                                            - - INDEX.md
                                                                                                              - - 01_xgboost_overview.md
                                                                                                                - - 02_second_order_optimization.md
                                                                                                                  - - 03_lightgbm_catboost.md
                                                                                                                    - - 04_industrial_applications.md
                                                                                                                      - - 05_interview_questions.md
                                                                                                                       
                                                                                                                        - PART 4: Dimensionality Reduction and Representation
                                                                                                                        - Target: 04-dimensionality-reduction/
                                                                                                                       
                                                                                                                        - Chapter 8: PCA
                                                                                                                        - Target Directory: 04-dimensionality-reduction/08-pca/
                                                                                                                       
                                                                                                                        - Files to Create:
                                                                                                                        - - INDEX.md
                                                                                                                          - - 01_eigendecomposition.md
                                                                                                                            - - 02_variance_explained.md
                                                                                                                              - - 03_geometric_interpretation.md
                                                                                                                                - - 04_real_world_applications.md
                                                                                                                                  - - 05_interview_questions.md
                                                                                                                                   
                                                                                                                                    - Chapter 9: LDA, ICA, Kernel PCA
                                                                                                                                    - Target Directory: 04-dimensionality-reduction/09-lda-ica-kernel-pca/
                                                                                                                                   
                                                                                                                                    - Files to Create:
                                                                                                                                    - - INDEX.md
                                                                                                                                      - - 01_linear_discriminant_analysis.md
                                                                                                                                        - - 02_independent_component_analysis.md
                                                                                                                                          - - 03_kernel_pca.md
                                                                                                                                            - - 04_comparisons_and_applications.md
                                                                                                                                              - - 05_interview_questions.md
                                                                                                                                               
                                                                                                                                                - Chapter 10: Manifold Learning
                                                                                                                                                - Target Directory: 04-dimensionality-reduction/10-manifold-learning/
                                                                                                                                               
                                                                                                                                                - Files to Create:
                                                                                                                                                - - INDEX.md
                                                                                                                                                  - - 01_manifold_hypothesis.md
                                                                                                                                                    - - 02_tsne_basics.md
                                                                                                                                                      - - 03_umap.md
                                                                                                                                                        - - 04_visualization_applications.md
                                                                                                                                                          - - 05_interview_questions.md
                                                                                                                                                           
                                                                                                                                                            - PART 5: Probabilistic Models and Latent Variables
                                                                                                                                                            - Target: 05-probabilistic-models/
                                                                                                                                                           
                                                                                                                                                            - Chapter 11: Bayesian Methods
                                                                                                                                                            - Target Directory: 05-probabilistic-models/11-bayesian-methods/
                                                                                                                                                           
                                                                                                                                                            - Files to Create:
                                                                                                                                                            - - INDEX.md
                                                                                                                                                              - - 01_bayesian_decision_theory.md
                                                                                                                                                                - - 02_bayes_theorem.md
                                                                                                                                                                  - - 03_naive_bayes.md
                                                                                                                                                                    - - 04_real_world_applications.md
                                                                                                                                                                      - - 05_interview_questions.md
                                                                                                                                                                       
                                                                                                                                                                        - Chapter 12: Gaussian Mixture Models and EM
                                                                                                                                                                        - Target Directory: 05-probabilistic-models/12-gmm-em/
                                                                                                                                                                       
                                                                                                                                                                        - Files to Create:
                                                                                                                                                                        - - INDEX.md
                                                                                                                                                                          - - 01_expectation_maximization.md
                                                                                                                                                                            - - 02_gaussian_mixture_models.md
                                                                                                                                                                              - - 03_em_convergence.md
                                                                                                                                                                                - - 04_real_world_applications.md
                                                                                                                                                                                  - - 05_interview_questions.md
                                                                                                                                                                                   
                                                                                                                                                                                    - Summary of Actions
                                                                                                                                                                                   
                                                                                                                                                                                    - Completed:
                                                                                                                                                                                    - - Part 1 INDEX.md: Linear Regression (INDEX.md)
                                                                                                                                                                                      - - Part 1 INDEX.md: Logistic Regression (INDEX.md)
                                                                                                                                                                                        - - Main README.md: Comprehensive guide
                                                                                                                                                                                          - - STRUCTURE_GUIDE.md: Full organizational documentation
                                                                                                                                                                                            - - FILE_ORGANIZATION_CHECKLIST.md: This file
                                                                                                                                                                                             
                                                                                                                                                                                              - To Complete:
                                                                                                                                                                                             
                                                                                                                                                                                              - Move Files (13 files total from root to Part 1):
                                                                                                                                                                                              - - 8 files -> 01-linear-models-geometry/01-linear-regression/
                                                                                                                                                                                                - - 5 files -> 01-linear-models-geometry/02-logistic-regression/
                                                                                                                                                                                                 
                                                                                                                                                                                                  - Create Remaining INDEX.md Files (10 total):
                                                                                                                                                                                                  - - 02-margin-based-learning/03-svm/INDEX.md
                                                                                                                                                                                                    - - 03-tree-ensembles/04-decision-trees/INDEX.md
                                                                                                                                                                                                      - - 03-tree-ensembles/05-random-forests/INDEX.md
                                                                                                                                                                                                        - - 03-tree-ensembles/06-boosting/INDEX.md
                                                                                                                                                                                                          - - 03-tree-ensembles/07-xgboost-lightgbm-catboost/INDEX.md
                                                                                                                                                                                                            - - 04-dimensionality-reduction/08-pca/INDEX.md
                                                                                                                                                                                                              - - 04-dimensionality-reduction/09-lda-ica-kernel-pca/INDEX.md
                                                                                                                                                                                                                - - 04-dimensionality-reduction/10-manifold-learning/INDEX.md
                                                                                                                                                                                                                  - - 05-probabilistic-models/11-bayesian-methods/INDEX.md
                                                                                                                                                                                                                    - - 05-probabilistic-models/12-gmm-em/INDEX.md
                                                                                                                                                                                                                     
                                                                                                                                                                                                                      - Create Placeholder Files (for chapters without content yet):
                                                                                                                                                                                                                      - - All chapters 3-12 need placeholder content files
                                                                                                                                                                                                                       
                                                                                                                                                                                                                        - Update Cross-References:
                                                                                                                                                                                                                        - - Update links in README.md files
                                                                                                                                                                                                                          - - Add links between related chapters
                                                                                                                                                                                                                            - - Create navigation within INDEX.md files
                                                                                                                                                                                                                             
                                                                                                                                                                                                                              - Expected Final Structure Count:
                                                                                                                                                                                                                              - - 5 main part directories
                                                                                                                                                                                                                                - - 12 chapter directories
                                                                                                                                                                                                                                  - - 12 INDEX.md files (one per chapter)
                                                                                                                                                                                                                                    - - 60+ content markdown files (5 per chapter minimum)
                                                                                                                                                                                                                                      - - Multiple README.md files for navigation
                                                                                                                                                                                                                                        - - Comprehensive documentation structure
                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                          - Organization Impact:
                                                                                                                                                                                                                                          - - Discoverability: Improved
                                                                                                                                                                                                                                            - - Learning Path Clarity: High
                                                                                                                                                                                                                                              - - Maintenance: Scalable
                                                                                                                                                                                                                                                - - Professional Appearance: Strong
                                                                                                                                                                                                                                                  - - User Experience: Intuitive navigation
