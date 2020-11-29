from die import Die
import pygal
import matplotlib.pyplot as plt


def main():
    # Create a D6.
    die = Die()

    # Make some rolls, and store results in a list.
    results = [die.roll() for _ in range(1000)]

    # Analyze the results.
    frequencies = [results.count(value) for value in range(1, die.num_sides() + 1)]

    # Visualize the results.
    hist = pygal.Bar()

    hist.title = "Results of rolling one D6 1000 times."
    hist.x_labels = [str(x) for x in range(1, die.num_sides() + 1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6', frequencies)
    hist.render_to_file('die_visual.svg')

    # Visualization with matplotlib pyplot
    plt.figure(figsize=(10, 6))
    plt.bar([str(x) for x in range(1, die.num_sides() + 1)], frequencies, width=0.5)
    plt.xlabel('Result', fontsize=14)
    plt.ylabel('Frequency of Result', fontsize=14)

    plt.show()


if __name__ == '__main__':
    main()
