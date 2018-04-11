import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

#question 1-2
#attached in canvas

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NORMAL)

# simulate the cohort
simOutputs = cohort.simulate()

#question 3
SupportMarkov.print_outcomes(simOutputs, 'NORMAL therapy:')

#question 4
A = P.ParametersFixed(P.Therapies.ANTI)
print("the transition prob matrix after Anticoagulation is:", A.get_transition_prob_whole())



#question 5
cohortTWO = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTI)

# simulate the cohort
simOutputsTWO = cohortTWO.simulate()

SupportMarkov.print_outcomes(simOutputsTWO, 'ANTI therapy:')


# question 6
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve NORMAL treatment',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )


PathCls.graph_sample_path(
    sample_path=simOutputsTWO.get_survival_curve(),
    title='Survival curve receiving ANTI treatment',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# question 7
Figs.graph_histogram(
    data=simOutputs.get_cohort_stroke(),
    title='Times of stroke of patients',
    x_label='Number of stroke during life time with NORMAL treatment',
    y_label='numbers',
)

Figs.graph_histogram(
    data=simOutputsTWO.get_cohort_stroke(),
    title='Times of stroke of patients',
    x_label='Number of stroke during life time with ANTI treatment',
    y_label='numbers',
)
