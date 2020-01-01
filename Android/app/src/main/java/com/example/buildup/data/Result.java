package com.example.buildup.data;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Result {
    @SerializedName("CategoryId")
    @Expose
    private Integer categoryId;
    @SerializedName("DesignInCategory")
    @Expose
    private List<DesignInCategory> designInCategory = null;
    @SerializedName("CategoryName")
    @Expose
    private String categoryName;

    public Integer getCategoryId() {
        return categoryId;
    }

    public void setCategoryId(Integer categoryId) {
        this.categoryId = categoryId;
    }

    public List<DesignInCategory> getDesignInCategory() {
        return designInCategory;
    }

    public void setDesignInCategory(List<DesignInCategory> designInCategory) {
        this.designInCategory = designInCategory;
    }

    public String getCategoryName() {
        return categoryName;
    }

    public void setCategoryName(String categoryName) {
        this.categoryName = categoryName;
    }
}
