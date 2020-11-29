from die import Die
import pygal


def main():
    # Create two dice.
    die_1 = Die(8)
    die_2 = Die(8)

    # Make some rolls, and store results in a list.
    results = [die_1.roll() + die_2.roll() for _ in range(1000)]

    # Analyze the results.
    max_result = die_1.num_sides() + die_2.num_sides()
    frequencies = [results.count(value) for value in range(2, max_result + 1)]

    # Visualize the results.
    hist = pygal.Bar()

    hist.title = "Results of rolling two D8 dice 10,000,000 times."
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D8 + D8', frequencies)
    hist.render_to_file('dice_visual.svg')


if __name__ == '__main__':
    main()
