/*
 * https://www.codewars.com/kata/515bb423de843ea99400000a
 */

package me.anviks.codewars.solutions._5kyu.paginationhelper;

import java.util.List;

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
            return (int) Math.floor(((double) itemIndex + 1) / itemsPerPage);
        } else {
            return -1;
        }
    }
}
