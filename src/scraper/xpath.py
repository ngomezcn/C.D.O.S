
class XpathCoingecko():
    class recently_added():
        coin_name = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/a[@class='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between']/text()"
        coin_href = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/a[@class='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between']/@href"
        id = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/span[@class='tw-hidden d-lg-inline font-normal text-3xs ml-2']/text()"
        time_since_added = "//td[@class='trade p-0 col-market pl-2 text-center']/text()"
            
    class token():
        contract = "//i/@data-address"
        chain = "//div[@class='tw-px-2.5 tw-flex tw-items-center tw-justify-center tw-py-1 tw-h-7 tw-my-0.5 tw-rounded-md  tw-text-sm tw-font-medium tw-bg-gray-100 tw-text-gray-800 dark:tw-text-white dark:tw-bg-opacity-10 hover:tw-bg-gray-200 dark:hover:tw-bg-opacity-20 tw-rounded-l-md']/span[@class='text-muted mr-2']/span/img/@src"
        price = "//div[@class='tw-text-4xl tw-font-bold tw-my-2 tw-flex tw-items-center']/span[@class='tw-text-gray-900 dark:tw-text-white tw-text-3xl']/span[@class='no-wrap']/text()"
class XpathPoocoin():
    class tokens():
        price = "//div[@class='d-flex align-items-start flex-wrap']/div[@class='mt-1 ps-2 d-flex align-items-center flex-grow-1']/div/div[@class='d-flex flex-wrap']/div[@class='mb-1 d-flex flex-column lh-1']/span[@class='text-success']/text()"
        market_cap = "//div[@id='root']/div[@class='d-flex flex-grow-1 bg-dark justify-content-center aos-init aos-animate']/div[@class='d-none d-md-flex flex-column flex-grow-1']/div[@class='d-flex flex-column flex-grow-1 pe-2']/div[@class='d-flex flex-grow-1 flex-row position-relative']/div[@class='TokenChart_stats__3732U d-block bg-dark-1 shadow pt-3 text-small']/div[@class='px-3']/span[@class='text-success']/text()[2]"
        total_supply = "//div[@id='root']/div[@class='d-flex flex-grow-1 bg-dark justify-content-center aos-init aos-animate']/div[@class='d-none d-md-flex flex-column flex-grow-1']/div[@class='d-flex flex-column flex-grow-1 pe-2']/div[@class='d-flex flex-grow-1 flex-row position-relative']/div[@class='TokenChart_stats__3732U d-block bg-dark-1 shadow pt-3 text-small']/div[@class='px-3']/text()[2]"