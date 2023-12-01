def read_input(input_path)
  File.readlines(input_path, chomp: true)
end

def part_a(input_path)
  lines = read_input(input_path)
  total_sum = 0

  lines.each do |line|
    first_digit = line.scan(/\d/).first
    last_digit = line.reverse.scan(/\d/).first
    total_sum += "#{first_digit}#{last_digit}".to_i
  end

  total_sum
end

def test_a
  part_a("test_input.txt") == 142
end

def part_b(input_path)
  numbers = {
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "four" => 4,
    "five" => 5,
    "six" => 6,
    "seven" => 7,
    "eight" => 8,
    "nine" => 9,
  }

  lines = read_input(input_path)
  total_sum = 0

  lines.each do |line|
    digits = []

    line.each_char.with_index do |char, i|
      digits << char.to_i if char =~ /\d/ # Regex matching

      numbers.each do |number, value|
        digits << value if line[i..-1].start_with?(number)
      end
    end

    total_sum += "#{digits.first}#{digits.last}".to_i
  end

  total_sum
end

def test_b
  part_b("test_input2.txt") == 281
end

puts "Test 1: #{test_a()}"
puts "Day 01a: #{part_a("input.txt")}"
puts "Test 2: #{test_b()}"
puts "Day 01b: #{part_b("input.txt")}"
