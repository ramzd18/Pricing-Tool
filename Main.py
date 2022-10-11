if __name__ == "__main__":
  sample = Prices()
  sample.system_get_function()
  inurl= sample.url_getter()
  total = sample.site_data_scrapper(inurl)
  sample.tocsv(total)
