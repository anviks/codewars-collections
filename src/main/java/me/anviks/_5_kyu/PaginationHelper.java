package me.anviks._5_kyu;

import java.util.List;

/**
 * <a href="https://www.codewars.com/kata/515bb423de843ea99400000a"><h2>PaginationHelper</h2></a>
 * <p>
 * For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class,
 * which is a utility class helpful for querying paging information related to an array.
 * </p>
 * <p>
 * The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page.
 * The types of values contained within the collection/array are not relevant.
 * </p>
 * <p>
 * The following are some examples of how this class is used:
 * </p>
 * <pre>
 * PaginationHelper<Character> helper = new PaginationHelper(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f'), 4);
 * helper.pageCount(); //should == 2
 * helper.itemCount(); //should == 6
 * helper.pageItemCount(0); //should == 4
 * helper.pageItemCount(1); // last page - should == 2
 * helper.pageItemCount(2); // should == -1 since the page is invalid
 *
 * // pageIndex takes an item index and returns the page that it belongs on
 * helper.pageIndex(5); //should == 1 (zero based index)
 * helper.pageIndex(2); //should == 0
 * helper.pageIndex(20); //should == -1
 * helper.pageIndex(-10); //should == -1
 * </pre>
 *
 * @param <I> type of items
 */
public class PaginationHelper<I> {

    List<I> items;
    int itemsPerPage;

    /**
     * The constructor takes in an array of items and an integer indicating how many
     * items fit within a single page
     */
    public PaginationHelper(List<I> collection, int itemsPerPage) {
        this.items = collection;
        this.itemsPerPage = itemsPerPage;
    }

    /**
     * returns the number of items within the entire collection
     */
    public int itemCount() {
        return this.items.size();
    }

    /**
     * returns the number of pages
     */
    public int pageCount() {
        return (int) Math.ceil(((double) this.items.size()) / itemsPerPage);
    }

    /**
     * returns the number of items on the current page. page_index is zero based.
     * this method should return -1 for pageIndex values that are out of range
     */
    public int pageItemCount(int pageIndex) {
        int count = items.size() - itemsPerPage * pageIndex;
        if (count < itemsPerPage) {
            return count <= 0 ? -1 : count;
        } else {
            return itemsPerPage;
        }
    }

    /**
     * determines what page an item is on. Zero based indexes
     * this method should return -1 for itemIndex values that are out of range
     */
    public int pageIndex(int itemIndex) {
        if (itemIndex < items.size() && itemIndex >= 0) {
            return (int) Math.ceil(((double) itemIndex + 1) / itemsPerPage);
        } else {
            return -1;
        }
    }

    public static void main(String[] args) {
        PaginationHelper paginationHelper = new PaginationHelper(List.of('a', 'b', 'c', 'd', 'e'), 4);
        System.out.println(paginationHelper.pageCount());
        System.out.println(paginationHelper.pageItemCount(1));
        System.out.println(paginationHelper.pageIndex(4));
    }
}