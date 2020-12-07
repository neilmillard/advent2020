from lib import get_lines_from_file


def answers_from_file_preserve_people(filepath='day6.txt'):
    groups = []
    lines = get_lines_from_file(filepath, True)
    entry = []
    for line in lines:
        if line.strip():
            entry.append(line.strip())
        else:
            groups.append(entry)
            entry = []

    return groups


def get_yes_from_group(groups, get_found=False):
    results = []
    for group in groups:
        found_letters = {}
        counter = 0
        for person in group:
            for letter in person:
                if letter not in found_letters:
                    counter += 1
                    found_letters[letter] = 1
                else:
                    found_letters[letter] += 1
        if get_found:
            answer_counter = 0
            for letter, count in found_letters.items():
                # if persons in group match the found count
                if count == len(group):
                    answer_counter += 1

            results.append(answer_counter)
        else:
            results.append(counter)

    return results


def get_dupe_yes_from_group(groups):
    return get_yes_from_group(groups, True)


def add_results(results):
    answer = 0
    for result in results:
        answer += result
    return answer


def day_six():
    groups = answers_from_file_preserve_people('day6/day6.txt')
    group_answers = get_yes_from_group(groups)
    print(group_answers)
    print(add_results(group_answers))

    person_groups = answers_from_file_preserve_people('day6/day6.txt')
    group_yes = get_dupe_yes_from_group(person_groups)
    print(group_yes)
    print(add_results(group_yes))
