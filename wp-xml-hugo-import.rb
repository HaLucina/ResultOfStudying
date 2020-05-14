# -*- coding: utf-8 -*-
# $ ruby wp-xml-hugo-import.rb ***.WordPress.2020-03-16.xml
require 'fileutils'
require 'time'
require 'rexml/document'
include REXML

class Time 
  def timezone(timezone = 'UTC')
    old = ENV['TZ']
    utc = self.dup.utc
    ENV['TZ'] = timezone
    output = utc.localtime
    ENV['TZ'] = old
    output
  end
end

doc = Document.new File.new(ARGV[0])
FileUtils.mkdir_p 'pc-related'
FileUtils.mkdir_p 'game'
FileUtils.mkdir_p 'life-theory'
FileUtils.mkdir_p 'others'
FileUtils.mkdir_p 'could_not_be_classified'


doc.elements.each("rss/channel/item[wp:post_type = 'post']") do |e|
	post = e.elements

  post_id   = post['wp:post_id'].text
  post_name = post['wp:post_name'].text  
  post_date = Time.parse(post['wp:post_date'].text)
  post_date.timezone('Asia/Tokyo')
  post_meta_decription = post['wp:postmeta[9]/wp:meta_value'] #9 => meta description 
  post_status = post['wp:status'].text
  title     = post['title'].text.gsub(/"/, '')
  content   = post['content:encoded'].text
  category  = ''
  jpCategory = ''

  # Replace absolute path to relative path
  # src="http://rakuishi.com/wp-content/uploads/2011/10/miso.jpg" → src="/images/2011/10/miso.jpg"
  content = content.gsub(/src="http:\/\/hackheatharu.xyz\/wp-content\/uploads\/(\d+)\/(\d+)\/(.+?)"/, 'src="/images/\1/\2/\3"')

  # [wp:status = publish] mean not draft 
  post_status == 'publish' ? post_status = "false" : post_status = "true"
  # Page not have category tag
  if defined?(post['category'].text)
    # My blog post have single category
    jpCategory = post['category'].text
    case jpCategory
      when 'PC関連' then
        category = 'pc-related'
      when 'ゲーム' then
        category = 'game'
      when '人生論' then
        category = 'life-theory'
      when 'その他' then
        category = 'others'
      else
        category = 'could_not_be_classified'
      end
  end
 
  begin
	 filename = "%02d-%02d-%02d-%04d-#{post_name}.md" % [post_date.year, post_date.month, post_date.day, post_id, post_name]
  rescue 
	  filename = "%02d-%02d-%02d-%04d-nothing.md" % [post_date.year, post_date.month, post_date.day, post_id]
  end
	 
  puts "[Converting]: #{filename}"
  puts "[path]: #{category}/#{filename}"
  File.open("#{category}/#{filename}", 'w') do |f|
    f.puts '---'
    f.puts "title: #{title}\n"
    f.puts "slug: #{post_name}\n"
    f.puts "date: #{post_date.strftime("%Y-%m-%dT%H:%M:%S%:z")}\n" # add +09:00 => Japan Standard Time
    if !jpCategory.empty?
      f.puts "categories: \n"
      f.puts " - #{jpCategory}\n"
    end
    f.puts "description: "
    f.puts "thumbnailImagePosition: left"
    f.puts "thumbnailImage: //d1u9biwaxjngwg.cloudfront.net/japanese-test-post/peak-140.jpg"
    f.puts "draft: #{post_status}"
    f.puts '---'
    f.puts "\n"
    f.puts "<!--more-->"
    f.puts "\n"
    f.puts content
  end
end
