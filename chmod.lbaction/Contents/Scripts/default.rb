#!/usr/bin/env ruby
#
# LaunchBar Action Script
#
puts '<?xml version="1.0"?>'
puts '<items>'

def oct_to_sym(x)
  num = x.to_i(8).to_s(2)
  result = ''
  result << (num.slice(0, 1) == '1' ? 'r' : '-')
  result << (num.slice(1, 1) == '1' ? 'w' : '-')
  result << (num.slice(2, 1) == '1' ? 'x' : '-')
  result
end

def sym_to_oct(x)
  x.gsub(/[rwx]/, '1').gsub('-', '0').to_i(2).to_s(8)
end

input = ARGV.first

if input =~ /[0-9]+/
  input  = input.slice 1, 3 if input.length >= 4
  owner  = oct_to_sym input.slice(0, 1)
  group  = oct_to_sym input.slice(1, 1)
  others = oct_to_sym input.slice(2, 1)
elsif input =~ /[drwx-]+/
  input  = input.slice 1, 9 if input.length >= 10
  owner  = input.slice 0, 3
  group  = input.slice 3, 3
  others = input.slice 6, 3
end

chmod = "chmod #{sym_to_oct(owner + group + others)}"
puts "  <item uid=\"octal\" valid=\"yes\" arg=\"#{chmod}\">"
puts "    <title>#{chmod}</title>"
puts '    <subtitle>Copy to clipboard</subtitle>'
puts '    <icon>icon.png</icon>'
puts '  </item>'
puts '  <item uid="owner">'
puts "    <title>Owner: #{owner}</title>"
puts '    <icon>owner.png</icon>'
puts '  </item>'
puts '  <item uid="group">'
puts "    <title>Group: #{group}</title>"
puts '    <icon>group.png</icon>'
puts '  </item>'
puts '  <item uid="others">'
puts "    <title>Others: #{others}</title>"
puts '    <icon>others.png</icon>'
puts '  </item>'

puts '</items>'